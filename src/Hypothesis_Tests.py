from utils import PlotJustifyText, PlotMarkdown, PlotImage

def Topics():
    return [
        ('Como os autores influenciam a avaliação?', HT1),
        ('Como o preço influencia a avaliação?', HT2),
        ('Impacto das avaliações na classificação "Best Seller"', HT3),
        ('Como o número de estrelas influencia no fato de ser um BestSeller', HT4),
        ('Como o fato de ser "IsKindleUnlimited" influencia no fato de um livro ser Best Seller', HT5),
        ('A categoria influencia em um livro ser Best Seller?', HT6)       
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
    
def HT4():
    PlotJustifyText("Vamos denotar a média de estrelas de best sellers por $E_m^{BS}$, e a média de estrelas de não best sellers por $E_m^{NBS}$. Portanto, podemos definir nossas hipóteses como:")
    
    PlotJustifyText("<b>Hipótese nula:</b> A média de estrelas de um best seller não é estatisticamente diferente da média de estrelas de um não best seller.")
    PlotJustifyText("<b>Hipótese alternativa:</b> Existe relação significativa entre a avaliação de um best seller e a avaliação de um não best seller.")
    
    PlotJustifyText('Estatística observável 0.089406')
    
    PlotImage('HT4.png')
    
    PlotMarkdown('Quartis inferior e superior 95%: [0.073348, 0.105047]')
    PlotMarkdown('Intervalo de confiança 95%: [0.089357, 0.089672]')
    
    PlotJustifyText("A nossa estatística observável de 0.0894 encontra-se dentro do intervalo de confiança. Portanto, o acaso explica a diferença entre o número médio de estrelas. Sendo assim, não rejeitamos a hipótese nula e podemos afirmar que o número médio de estrelas não afeta o fato de um livro ser um best seller.")
    
def HT5():   
    PlotJustifyText("<b>Hipótese nula:</b> Não há diferença na proporção de Best Sellers entre livros que fazem parte do Kindle Unlimited e aqueles que não fazem parte. Isso significa que a diferença média observada no bootstrapping (D = 0) é devido ao acaso.")
    PlotJustifyText("<b>Hipótese alternativa:</b> Há uma diferença na proporção de Best Sellers entre livros que fazem parte do Kindle Unlimited e aqueles que não fazem parte. Isso significa que a diferença média observada no bootstrapping (D ≠ 0) não é apenas devido ao acaso.")
        
    PlotImage('HT5.png')
    
    PlotMarkdown('Quantis 2.5% e 97.5%: [0.0308654935155852, 0.035217891848341835]')
    PlotMarkdown('Intervalo de Confiança: [0.03287641063436545, 0.03301593857822303]')
    PlotMarkdown('Estatística Observável = 0.0329796434937253')
    
    PlotJustifyText("Dado que o intervalo de confiança (0.03280, 0.03320) não inclui zero e é relativamente estreito, podemos concluir que há evidências estatisticamente significativas que sugerem que fazer parte do Kindle Unlimited aumenta a chance de um livro se tornar um bestseller. A estatística observável (est_obs) de 0.03298 indica que os livros do Kindle Unlimited têm cerca de 3,3% mais probabilidade de serem bestsellers em comparação com os livros que não são do Kindle Unlimited, e essa diferença é estatisticamente significativa.")
    
def HT6():
    PlotJustifyText("<b>Hipótese nula:</b> Não há diferença significativa no número de Best Sellers entre as diferentes categorias. Ou seja, a diferença observada entre o valor nos dados reais e o valor nos dados simulados é atribuível ao acaso. Se o valor observado nos dados reais estiver dentro do intervalo de valores gerados pelos dados simulados, aceitamos a hipótese nula, indicando que a categoria não influencia significativamente na probabilidade de um livro ser um Best Seller.")
    PlotJustifyText("<b>Hipótese alternativa:</b> Há uma diferença significativa no número de Best Sellers entre as diferentes categorias. Ou seja, a diferença entre o valor observado nos dados reais e o valor nos dados simulados não é atribuível ao acaso, indicando que a categoria tem uma influência significativa na probabilidade de um livro ser um Best Seller.")
        
    PlotImage('HT6.png')
    PlotImage('HT7.png')
      
    PlotJustifyText("Com os testes de permutação, tornamos aleatório a categoria de um livro ser Best Seller ou não, assumindo apenas que essas váriaveis fazem parte da análise para ser BestSeller. Com isso após cada permutação, é feita uma contagem de BestSellers por categoria e é subtraído o valor observado origal e armazenado em uma matriz. Feito isso, plotamos os histogramas com os valores simulados primeiras categorias mais frequentes. Como é possível observar, as diferenças entre os valores não estão centrados em 0, ou seja, nos dados atuais, a categoria influência ser um Best Seller, ja que a quantia de Best Sellers continua a mesma, o que muda é a aleatoriedade de uma categoria ser Best Seller ou não.")
