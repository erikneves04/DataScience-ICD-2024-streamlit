import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
from utils import PlotJustifyText, PlotGraph, LoadDatabases
sns.set_theme()

#Setando o tamanho padrão das figuras
matplotlib.rcParams['figure.figsize'] = (15.0, 9.0)

# Acessos aos dados
kindle_data, books = LoadDatabases()

def Topics():
    return [
        ('Preços x Avaliações', AE1),
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