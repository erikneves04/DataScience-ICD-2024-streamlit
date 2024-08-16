from utils import PlotJustifyText, PlotGraph, LoadDatabases

import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
sns.set_theme()

#Setando o tamanho padrão das figuras
matplotlib.rcParams['figure.figsize'] = (15.0, 9.0)

# Acessos aos dados
kindle_data, books = LoadDatabases()

def Topics():
    return [
        ('Preços x Avaliações', AE1),
        ('Autores x Avaliações', AE2),
        ('Best Seller x Avaliações', AE3),
    ]

def AE1():
    PlotJustifyText("Nesse tópico buscamos avaliar se existe uma relação entre o preço de um livro e suas avaliação média. Para realizar essa análise vamos nos basear na média de preços e em um arredondamento das avaliações(que serão agrupadas de 0 a 5 e com seus decimais intermediários -- 0.5). Além disso serão exibidos dois cenários, um com os dados originais e outro com 95% dos dados, visando reduzir a influência de dados extremos e fora do normal(outliers) na visualização.")
    
    # Adicionando uma nova coluna 'RoundedStars' para arredondar as estrelas para o meio mais próximo
    decimal_values = np.modf(kindle_data['Stars'])[0]
    int_values = kindle_data['Stars'] - decimal_values
    kindle_data['RoundedStars'] = np.where(
        decimal_values <= 0.3,
        int_values,
        np.where(decimal_values >= 0.7, int_values + 1, int_values + 0.5)
    )

    # Removendo outliers com base nos percentis
    lower_bound = np.percentile(kindle_data['Price'], 2.5)
    upper_bound = np.percentile(kindle_data['Price'], 97.5)
    df_no_outliers = kindle_data[(kindle_data['Price'] >= lower_bound) & (kindle_data['Price'] <= upper_bound)]

    # Calculando a média dos preços agrupados pelas estrelas arredondadas
    series = kindle_data[['RoundedStars', 'Price']].groupby('RoundedStars').mean()
    series_no_outliers = df_no_outliers[['RoundedStars', 'Price']].groupby('RoundedStars').mean()
    
    fig, axs = plt.subplots(1, 2, figsize=(18, 6), sharey=True)

    # Gráfico com todos os dados
    sns.lineplot(x=series.index, y=series['Price'], marker='o', color='b', ax=axs[0])
    axs[0].set_xlabel('Stars', fontsize=14)
    axs[0].set_ylabel('Average Price (R$)', fontsize=14)
    axs[0].set_title('Preço Médio vs. Avaliação', fontsize=16)
    axs[0].tick_params(axis='both', which='major', labelsize=12)

    # Gráfico sem outliers
    sns.lineplot(x=series_no_outliers.index, y=series_no_outliers['Price'], marker='o', color='b', ax=axs[1])
    axs[1].set_xlabel('Stars', fontsize=14)
    axs[1].set_title('Preço Médio vs. Avaliação (sem Outliers)', fontsize=16)
    axs[1].tick_params(axis='both', which='major', labelsize=12)

    PlotGraph(plt)
    plt.close()
    PlotJustifyText("De acordo com os gráficos acima não temos nenhuma indicação de que exista uma relação entre essas duas variáveis, sendo assim, será necessário partir para uma segunda análise. Na segunda etapa, que será abordada em outro notebook, buscamos quebrar a associação entre preço e avaliação aplicando um teste de permutação em amostras reduzidas dos dados.")

def AE2():
    PlotJustifyText("Neste tópico buscamos avaliar se existe uma relação entre o número de publicações de um autor e sua avaliação média. Para realizar essa análise, vamos nos basear na média do número de publicações e em um arredondamento das avaliações que fizemos anteriormente.")

    # Calculando o número de publicações por autor
    publications_per_author = kindle_data['Authors'].value_counts().reset_index()
    publications_per_author.columns = ['Authors', 'Publications']

    # Calculando a média das avaliações por autor
    average_stars_per_author = kindle_data.groupby('Authors')['RoundedStars'].mean().reset_index()

    # Combinando os dados de publicações e avaliações
    author_stats = pd.merge(publications_per_author, average_stars_per_author, on='Authors')

    fig, axs = plt.subplots(1, 2, figsize=(18, 6), gridspec_kw={'width_ratios': [2, 2]})

    # Gráfico de dispersão
    sns.scatterplot(x='RoundedStars', y='Publications', data=author_stats, ax=axs[0], alpha=0.5, color='b')
    axs[0].set_xlabel('Avaliação Média', fontsize=14)
    axs[0].set_ylabel('Número de Publicações', fontsize=14)
    axs[0].set_title('Número de Publicações vs. Avaliação Média', fontsize=16)
    axs[0].tick_params(axis='both', which='major', labelsize=12)

    # Histograma das avaliações médias
    sns.histplot(author_stats['RoundedStars'], bins=np.arange(0, 5.5, 0.5), ax=axs[1], alpha=0.7, color='b', edgecolor='black')
    axs[1].set_xlabel('Avaliação Média', fontsize=14)
    axs[1].set_ylabel('Frequência', fontsize=14)
    axs[1].set_title('Distribuição das Avaliações Médias', fontsize=16)
    axs[1].tick_params(axis='both', which='major', labelsize=12)

    plt.tight_layout()
    PlotGraph(plt)
    plt.close()
    PlotJustifyText("Esse resultado pode ser explicado pelo fato de que avaliações no geral tendem a ser boas, refletindo uma tendência positiva dos leitores ao avaliar livros. Além disso, novos autores com poucas publicações podem lançar obras de alta qualidade que recebem grande apreciação do público, ou podem ter uma base de leitores inicial que é particularmente entusiasta e generosa nas avaliações.")
def AE3():
    best_sellers = kindle_data.query('IsBestSeller == True')

    fig = sns.histplot(data=best_sellers, x='Stars', kde=True)
    plt.xlabel('Estrelas')
    plt.ylabel('Quantidade de best sellers')
    plt.show()
    PlotGraph(plt)
    plt.close()
