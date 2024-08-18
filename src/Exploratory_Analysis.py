from utils import PlotJustifyText, PlotGraph, LoadDatabases

import pandas as pd
import streamlit as st
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
        ('Distribuição dos lançamentos', AE4),
        ('Distribuição dos preços', AE5),
        ('Relação de IsBestSeller com preço', AE6)
        ('Relação da Categoria e IsBestSeller', AE7),
        ('Relação de IsKindleUnlimited e IsBestSeller', AE8),
        ('Categoria mais vendida por Ano', AE9)
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
    # Calculando a média das estrelas
    mean_stars = best_sellers['Stars'].mean()

    # Exibindo a média das estrelas no Streamlit
    st.metric(label="Média das Estrelas dos Best Sellers", value=f"{mean_stars:.2f}")
    
    PlotJustifyText("Com base no gráfico e na estatística observada, livros que são Best Seller tem entre 4 e 5 estrelas, com média de aproximadamente 4,5 estrelas. Isso não é estranho, visto que a próprio conceito de 'BestSeller' carrega essa característica de ter uma avaliação boa, de modo geral.")


def AE4():
    # Convertendo a coluna de datas (string) para um objeto datetime 
    meses_publicacao = pd.to_datetime(kindle_data['PublishDate'], errors='coerce') # Retorna uma Panda Series
    kindle_data['PublishMonth'] = meses_publicacao.dt.month

    # Todos os livros lancados no mês
    lancamentos_total_meses = kindle_data.groupby('PublishMonth', as_index=False)[['AmazonID']].count() 

    # Todos os best sellers lançados no mês
    lancamentos_BS_meses = kindle_data.query('IsBestSeller == True')\
        .groupby('PublishMonth', as_index=False)[['AmazonID']].count()

    # Todos os livros não-best sellers lançados no mês
    lancamentos_nonBS_meses = kindle_data.query('IsBestSeller == False')\
        .groupby('PublishMonth', as_index=False)[['AmazonID']].count()

    # Criando um dataframe para armazenar os valores agregados
    lancamentos_agregados = pd.DataFrame({'Mes': [],'Totais': [], 'BestSellers': [], 'NonBestSellers': []})
    lancamentos_agregados['Mes'] = lancamentos_total_meses['PublishMonth']
    lancamentos_agregados['Totais'] = lancamentos_total_meses['AmazonID']
    lancamentos_agregados['BestSellers'] = lancamentos_BS_meses['AmazonID']
    lancamentos_agregados['NonBestSellers'] = lancamentos_nonBS_meses['AmazonID']

    lancamentos_agregados.set_index('Mes', inplace=True)

    fig = sns.lineplot(data=lancamentos_agregados, dashes=False, palette='rocket', markers=True)
    plt.xlabel('Mês')
    plt.ylabel('Montante de livros')
    plt.show()
    PlotGraph(plt)
    plt.close()

def AE5():     
    # Filtrando dados
    df_filtered = kindle_data[(kindle_data['Price'] >= 0) & (kindle_data['Price'] <= 100)]

    fig, axs = plt.subplots(1, 2, figsize=(18, 6), gridspec_kw={'width_ratios': [2, 2]})

    # Histograma da distribuição de preços
    sns.histplot(kindle_data['Price'], bins=20, color='b', edgecolor='black', alpha=0.7, ax=axs[0])
    axs[0].set_xlabel('Preço', fontsize=14)
    axs[0].set_ylabel('Quantidade', fontsize=14)
    axs[0].set_title('Distribuição de Preços', fontsize=16)
    axs[0].tick_params(axis='both', which='major', labelsize=12)

    # Histograma da distribuição de preços entre 0 e 100
    sns.histplot(df_filtered['Price'], bins=20, color='b', edgecolor='black', alpha=0.7, ax=axs[1])
    axs[1].set_xlabel('Preço', fontsize=14)
    axs[1].set_ylabel('Quantidade', fontsize=14)
    axs[1].set_title('Distribuição de Preços (0-100)', fontsize=16)
    axs[1].tick_params(axis='both', which='major', labelsize=12)

    plt.tight_layout()
    plt.show()
    PlotGraph(plt)
    plt.close()
    
    PlotJustifyText("A análise dos histogramas revela que a maior parte dos livros tem preços concentrados entre 0 e 20 dólares. Essa concentração sugere que a faixa de preço mais acessível é bastante popular entre os consumidores, possivelmente devido à sua atratividade financeira e à acessibilidade para um público mais amplo. Essa concentração pode refletir estratégias de precificação adotadas por editores e autores para alcançar um público maior e maximizar as vendas.")

def AE6():
    
    PlotJustifyText("Nesse tópico buscamos avaliar se existe uma relação entre o preço de um livro e se ele foi Best Seller. Para realizar essa análise vamos nos basear em faixas de preços e verificar em qual faixa se concentra mais os livros que foram Best Seller.")
    
    df = kindle_data

    # Calculando o preço máximo e mínimo
    preco_maximo = df['Price'].max()
    preco_minimo = df['Price'].min()

    # Exibindo os valores no Streamlit
    st.write("O preço máximo é:", preco_maximo)
    st.write("O preço mínimo é:", preco_minimo)

    # Ou, se preferir exibir como métricas visuais
    st.metric(label="Preço Máximo", value=f"${preco_maximo:.2f}")
    st.metric(label="Preço Mínimo", value=f"${preco_minimo:.2f}")
    
    # Definindo as faixas de preço. Usando 50 reais de range para cada.
    bins = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700]
    labels = [f'{bins[i]}-{bins[i+1]}' for i in range(len(bins)-1)]

    # Classifica os preços em intervalos
    df['Price Range'] = pd.cut(df['Price'], bins=bins, labels=labels)

    # Filtra somente os Best Sellers e faz a contagem
    best_seller = df[df['IsBestSeller']]
    price_of_best_sellers = best_seller['Price Range'].value_counts().sort_index()

    # Contando a quantidade de produtos em cada faixa de preço
    price_range_counts = best_seller['Price Range'].value_counts().sort_index()

    # Plotando os graficos em escala normal e logaritmica para ver melhor
    # Gráfico com escala normal
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

    sns.barplot(x=price_range_counts.index, y=price_range_counts.values, ax=axes[0], palette='muted')
    axes[0].set_xlabel('Faixa de Preço')
    axes[0].set_ylabel('Quantidade de Livros')
    axes[0].set_title('Distribuição de Produtos por Faixa de Preço (Escala Normal)')
    axes[0].set_xticklabels(labels, rotation=45)

    best_seller_0_to_70 = best_seller[best_seller['Price'] <= 70]

    # Histograma com as faixas de preço de 0 a 70
    sns.histplot(best_seller_0_to_70['Price'], bins=30, ax=axes[1], kde=False, color='skyblue', edgecolor='black')
    axes[1].set_xlabel('Faixa de Preço')
    axes[1].set_ylabel('Quantidade de Livros')
    axes[1].set_title('Histograma por Faixa de Preço (0 a 70)')
    axes[1].set_xticks(range(0, 70, 5))

    plt.tight_layout()
    plt.show()
    PlotGraph(plt)
    plt.close()
    PlotJustifyText("Analisando o Gráfico anterior, a faixa de preço predominantemente com livros Best Sellers é de 0 a 50 reais. Provavelmente, isso não é explicado pelo acaso, visto que a faixa de preço é relativamente baixa, o que pode gerar mais vendas, mas será bom testar para ver se a relação com o acaso ou não.Além disso, com o histograma, verificamos que os livros que custam 5 reais são os mais vendidos.")
    
def AE7():
    
    PlotJustifyText("Nesse tópico buscamos avaliar se existe uma relação entre a Categoria de um livro e Best Seller, para ver quais categorias com mais Best Sellers. Para realizar essa análise vamos verificar em qual categoria se concentra mais os livros que foram Best Seller.")
    
    # Selecionando somente os livros que são Best Sellers e selecionando apenas a Coluna Categoria
    df = kindle_data
    best_sellers = df[df['IsBestSeller']]['Category']

    # Contando a quantia de Best Sellers
    category_counts = best_sellers.value_counts()

    # Criando o gráfico
    fig, ax = plt.subplots(figsize=(18, 10))
    sns.barplot(y=category_counts.index, x=category_counts.values, ax=ax, palette='muted')
    ax.set_xlabel('Quantidade de Produtos')
    ax.set_ylabel('Categoria')
    ax.set_title('Distribuição de Produtos por Categoria')

    plt.tight_layout()
    plt.show()
    PlotGraph(plt)
    plt.close()
    PlotJustifyText("Nessa parte, as 3 principais categorias são 'Literature & Fiction', 'Science & Math' e 'Children's eBooks'. Literatura e Ficção pode ser explicado por ser um gênero que alcança todas as faixas etárias de idade. Matemática e Ciência geraram pesquisas no Google, as quais nos levaram a crer que esse genêro está no TOP 2 por ser livro que aborda aspectos da ciência de forma literária, como o livro Technology and Society: A Critical Analysis of 'The Coming Wave', que fala sobre as oportunidades e desafios trazidos pela Era Moderna. Esse tópico é interessante por si só, por trazer conhecimento de diversas formas, que não seja acadêmico. Livros para criança também é fácil de gerar uma hipotese, visto que a população mundial de crianças chega a 1/4 da população mundial total. Após essa pequena análise, vamos focar nos testes para ver se o acaso explica isso. Caso acaso não explique, nossa teoria pode estar certa.")

def AE8():

    PlotJustifyText("Nesse tópico buscamos entender se existe uma relação entre ser Best Seller e Kindle Unlimited. Para analisar agregaremos todos os Best Sellers e checar a frequência que pertence ao Kindle Unlimited.")
    
    df = kindle_data

    # Filtra o dataframe para obter os best sellers
    best_sellers = df[df['IsBestSeller']]

    # Calcula as proporções
    kindle_unlimited_counts = best_sellers['IsKindleUnlimited'].value_counts()
    total_best_sellers = kindle_unlimited_counts.sum()
    kindle_unlimited_prob = kindle_unlimited_counts / total_best_sellers

    # Plotagem
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=kindle_unlimited_prob.index, y=kindle_unlimited_prob.values, ax=ax, palette='muted')
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['Outros', 'Kindle Unlimited'])
    ax.set_xlabel('Classificação')
    ax.set_ylabel('Probabilidade')
    ax.set_title('Chance de ser Kindle Unlimited para Best Sellers')
    plt.show()
    PlotGraph(plt)
    plt.close()
    
    PlotJustifyText("A observação de que a maioria dos livros Best Seller é Kindle Unlimited sugere uma possível influência do programa Kindle Unlimited (KU) nos rankings de best sellers da Amazon. Isso pode indicar que o algoritmo da Amazon favorece ou dá maior visibilidade a livros que fazem parte desse programa.")


def AE9():

    df = kindle_data

    start_year = '2000'

    # Converter a coluna 'PublishDate' para datetime, ignorando valores inválidos
    df['PublishDate'] = pd.to_datetime(df['PublishDate'], errors='coerce')

    # Remover linhas onde 'PublishDate' é NaT
    df = df.dropna(subset=['PublishDate'])

    # Extrair o ano da data de publicação
    df['Year'] = df['PublishDate'].dt.year

    # Filtrar para incluir apenas livros publicados a partir de 2000
    df = df[df['Year'] >= int(start_year)]

    # Agrupar por 'Category' e 'Year', calcular a média de preço e contar o número de livros
    category_and_year_grouped = df.groupby(['Category', 'Year']).agg({'Price': 'mean', 'PublishDate': 'size'}).reset_index()
    category_and_year_grouped.rename(columns={'PublishDate': 'Count'}, inplace=True)

    # Identificar a categoria com a maior média de preço para cada ano
    idx = category_and_year_grouped.groupby(['Year'])['Price'].idxmax()
    highest_avg_price_category = category_and_year_grouped.loc[idx]

    # Criar o gráfico de barras horizontal usando Seaborn
    plt.figure(figsize=(15, 7))
    sns.barplot(
        x=highest_avg_price_category['Price'],
        y=highest_avg_price_category['Year'],
        orient='h',
        palette='Blues_d'
    )

    # Adicionar legenda para indicar a categoria mais popular
    for i, (price, category) in enumerate(zip(highest_avg_price_category['Price'], highest_avg_price_category['Category'])):
        plt.text(price, i, category, va='center')

    plt.ylabel('Year')
    plt.xlabel('Average Price ($)')
    plt.title('Categorias com livros mais vendidos a partir de 2000')
    plt.show()
    PlotGraph(plt)
    plt.close()