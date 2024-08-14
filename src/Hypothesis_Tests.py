from utils import PlotJustifyText, PlotGraph, LoadDatabases, PlotMarkdown

import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns

sns.set_theme()

# Setando o tamanho padrão das figuras
matplotlib.rcParams['figure.figsize'] = (15.0, 9.0)

# Acessos aos dados
kindle_data, books = LoadDatabases()

def Topics():
    return [
        ('Como os autores influenciam a avaliação?', HT1),
        ('Como o preço influencia a avaliação?', HT2),
        ('Impacto das avaliações na classificação "Best Seller"', HT3)
    ]

def HT1():
    PlotMarkdown("<b>Hipótese nula:</b> Não há diferença significativa nas avaliações dos livros com base no autor. Ou seja, as avaliações atribuídas aos livros não são influenciadas pelo autor que os escreveu.")
    PlotMarkdown("<b>Hipótese alternativa:</b> Existe uma diferença significativa nas avaliações dos livros com base no autor. Ou seja, o autor influencia as avaliações atribuídas aos livros.")

    # Cálculo da Estatística Observada
    group_means = kindle_data.groupby('Authors')['Stars'].mean()
    overall_mean = kindle_data['Stars'].mean()

    between_group_variance = ((group_means - overall_mean) ** 2).sum()

    # Número de amostras de bootstrap
    num_bootstrap = 1000

    # Lista para armazenar as estatísticas de bootstrap
    bootstrap_stats = []

    # Execução do Bootstrap
    for _ in range(num_bootstrap):
        bootstrap_sample = kindle_data.sample(frac=0.05, replace=True)
        group_means_bootstrap = bootstrap_sample.groupby('Authors')['Stars'].mean()
        overall_mean_bootstrap = bootstrap_sample['Stars'].mean()
        between_group_variance_bootstrap = ((group_means_bootstrap - overall_mean_bootstrap) ** 2).sum()
        bootstrap_stats.append(between_group_variance_bootstrap)

    # Conversão da lista de estatísticas para um array numpy
    bootstrap_stats = np.array(bootstrap_stats)

    # Cálculo do intervalo de confiança de 95%
    conf_interval = np.percentile(bootstrap_stats, [2.5, 97.5])

    # Impressão dos resultados
    PlotJustifyText(f'Estatística Observada: {between_group_variance:.3f}')
    PlotMarkdown(f'Intervalo de Confiança de 95%: [{conf_interval[0]:.3f}, {conf_interval[1]:.3f}]')

    # Plotar os resultados
    sns.histplot(bootstrap_stats, bins=30, alpha=0.7)
    plt.axvline(between_group_variance, color='red', linestyle='--', linewidth=2, label=f'Estatística Observada: {between_group_variance:.2f}')
    plt.axvline(conf_interval[0], color='green', linestyle='--', linewidth=2, label=f'2.5% Percentil: {conf_interval[0]:.2f}')
    plt.axvline(conf_interval[1], color='green', linestyle='--', linewidth=2, label=f'97.5% Percentil: {conf_interval[1]:.2f}')
    plt.xlabel('Variância entre Grupos Bootstrap')
    plt.ylabel('Frequência')
    plt.title('Teste de Hipótese Bootstrap para Avaliação de Autores')
    plt.legend()
    plt.xlim(0, conf_interval[1] * 1.5)
    plt.show()
    
    PlotGraph(plt)
    PlotJustifyText("A estatística observada de 53926,66 é significativamente maior do que o intervalo de confiança bootstrap (aproximadamente, 2960 a 3860), indicando que a variância entre as médias das avaliações dos autores não é atribuída ao acaso. O método bootstrap permite rejeitar a hipótese nula com alta confiança. Esse resultado sugere que fatores como estilo de escrita e engajamento com os leitores fazem com que autores bem avaliados escrevam livros que consistentemente agradam ao público.")

def HT2():
    PlotMarkdown("<b>Hipótese nula:</b> Não há relação significativa entre o preço e a avaliação dos livros. Ou seja, o preço não influencia as avaliações atribuídas pelos leitores.")
    PlotMarkdown("<b>Hipótese alternativa:</b> Existe uma relação significativa entre o preço e a avaliação dos livros. Ou seja, o preço influencia as avaliações atribuídas pelos leitores.")

    observed_stat = np.corrcoef(kindle_data['Price'], kindle_data['Stars'])[0, 1]

    # Gerarando as amostras e calculando a correlação
    bootstrap_stats = []
    for _ in range(1000):
        bootstrap_sample = kindle_data.sample(frac=0.05, replace=True)
        bootstrap_stat = np.corrcoef(bootstrap_sample['Price'], bootstrap_sample['Stars'])[0, 1]
        bootstrap_stats.append(bootstrap_stat)

    bootstrap_stats = np.array(bootstrap_stats)

    # Plotar os resultados
    sns.histplot(data=bootstrap_stats, bins=30, alpha=0.7)
    plt.axvline(x=observed_stat, color='red', linestyle='--', linewidth=2, label=f'Correlação Observada: {observed_stat:.2f}')
    plt.xlabel('Coeficiente de Correlação Bootstrap')
    plt.ylabel('Frequência')
    plt.title('Teste de Hipótese: Preço vs Avaliação')
    plt.legend()
    
    PlotGraph(plt)
    PlotJustifyText("O gráfico acima mostra a distribuição dos coeficientes de correlação obtidos através do método bootstrap para avaliar a relação entre o preço e a avaliação (estrelas). A correlação observada entre preço e avaliação é de -0.13, indicada pela linha vermelha pontilhada. Essa correlação negativa muito fraca sugere que não há uma relação linear significativa entre essas duas variáveis no conjunto de dados analisado. A distribuição bootstrap confirma essa observação, pois está centrada em torno de -0.13, indicando que variações no preço não estão fortemente associadas a variações nas avaliações.")

def HT3():
    PlotJustifyText("<b>Hipótese nula:</b> A média de estrelas de um best seller não é estatisticamente diferente da média de estrelas de um não best seller.")
    PlotJustifyText("<b>Hipótese alternativa:</b> Existe relação significativa entre a avaliação de um best seller e a avaliação de um não best seller.")
    data = kindle_data[['Stars', 'IsBestSeller']]

    # Estatística observável = diferença entre a média de estrelas de best sellers e a média de estrelas de não best sellers
    est_obs = data[data.IsBestSeller == True].Stars.mean() - data[data.IsBestSeller == False].Stars.mean()

    #Bootstrap
    acasos = []
    for i in range(1000):
        data_sample = data.sample(len(data), replace=True)
        filtro = data_sample.IsBestSeller == True
        d = data_sample[filtro].Stars.mean() - data_sample[~filtro].Stars.mean()
        acasos.append(d)

    # Quantis da distribuição
    q_025 = np.percentile(acasos, 2.5)
    q_975 = np.percentile(acasos, 97.5) 

    # Contruindo o intervalo de confiança
    erro_padrao = np.std(acasos) / np.sqrt(len(acasos))
    media = np.mean(acasos)
    intervalo_de_confianca = media - 1.96 * erro_padrao, media + 1.96 * erro_padrao

    PlotJustifyText(f"Estatística observável {est_obs:0.6f}")

    PlotJustifyText(f"Quantis da distribuição: [{q_025:0.6f}, {q_975:0.6f}]")

    PlotJustifyText(f"Intervalo de confiança: [{intervalo_de_confianca[0]:0.6f}, {intervalo_de_confianca[1]:0.6f}]")

    sns.histplot(data=acasos)\
    .set(xlabel='$E_m^{BS}-E_m^{NBS}$', ylabel='Quantidade')

    PlotGraph(plt)

    PlotJustifyText("A nossa estatística observável de 0.0894 encontra-se dentro do intervalo de confiança. Portanto, o acaso explica a diferença entre o número médio de estrelas. Sendo assim, não rejeitamos a hipótese nula e podemos afirmar que o número médio de estrelas não afeta o fato de um livro ser um best seller.")