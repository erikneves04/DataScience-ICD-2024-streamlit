from utils import PlotJustifyText, PlotMarkdown, PlotImage

def Topics():
    return [
        ('Como os autores influenciam a avaliação?', HT1),
        ('Como o preço influencia a avaliação?', HT2),
        ('Impacto das avaliações na classificação "Best Seller"', HT3)
    ]

def HT1():
    PlotMarkdown("<b>Hipótese nula:</b> Não há diferença significativa nas avaliações dos livros com base no autor. Ou seja, as avaliações atribuídas aos livros não são influenciadas pelo autor que os escreveu.")
    PlotMarkdown("<b>Hipótese alternativa:</b> Existe uma diferença significativa nas avaliações dos livros com base no autor. Ou seja, o autor influencia as avaliações atribuídas aos livros.")

    PlotJustifyText('Estatística Observável: 53926.664608')
    PlotMarkdown('Intervalo de Confiança de 95%: [2936.715894, 3840.589003]')

    PlotImage('HT1.png')
    
    PlotJustifyText("A estatística observada de 53926,66 é significativamente maior do que o intervalo de confiança bootstrap (aproximadamente, 2960 a 3860), indicando que a variância entre as médias das avaliações dos autores não é atribuída ao acaso. O método bootstrap permite rejeitar a hipótese nula com alta confiança. Esse resultado sugere que fatores como estilo de escrita e engajamento com os leitores fazem com que autores bem avaliados escrevam livros que consistentemente agradam ao público.")

def HT2():
    PlotMarkdown("<b>Hipótese nula:</b> Não há relação significativa entre o preço e a avaliação dos livros. Ou seja, o preço não influencia as avaliações atribuídas pelos leitores.")
    PlotMarkdown("<b>Hipótese alternativa:</b> Existe uma relação significativa entre o preço e a avaliação dos livros. Ou seja, o preço influencia as avaliações atribuídas pelos leitores.")

    PlotJustifyText('Correlação Observável: -0.126705')
    PlotMarkdown('Intervalo de Confiança de 95%: [-0.175363, -0.078255]')

    PlotImage('HT2.png')

    PlotJustifyText("O gráfico acima mostra a distribuição dos coeficientes de correlação obtidos através do método bootstrap para avaliar a relação entre o preço e a avaliação (estrelas). A correlação observada entre preço e avaliação é de -0.13, indicada pela linha vermelha pontilhada. Essa correlação negativa muito fraca sugere que não há uma relação linear significativa entre essas duas variáveis no conjunto de dados analisado. A distribuição bootstrap confirma essa observação, pois está centrada em torno de -0.13, indicando que variações no preço não estão fortemente associadas a variações nas avaliações.")

def HT3():
    PlotJustifyText("<b>Hipótese nula:</b> A média de estrelas de um best seller não é estatisticamente diferente da média de estrelas de um não best seller.")
    PlotJustifyText("<b>Hipótese alternativa:</b> Existe relação significativa entre a avaliação de um best seller e a avaliação de um não best seller.")
    
    PlotJustifyText('Estatística observável 0.089406')
    PlotMarkdown('Intervalo de confiança 95%: [0.015517, 0.149543]')

    PlotImage('HT3.png')

    PlotJustifyText("A nossa estatística observável de 0.0894 encontra-se dentro do intervalo de confiança. Portanto, o acaso explica a diferença entre o número médio de estrelas. Sendo assim, não rejeitamos a hipótese nula e podemos afirmar que o número médio de estrelas não afeta o fato de um livro ser um best seller.")