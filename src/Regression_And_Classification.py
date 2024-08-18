from utils import PlotJustifyText, PlotMarkdown, PlotImage

def Topics():
    return [
       ('Autores e avaliações', RC1),
       ('Classificando Avaliações', RC2),
       ('Analisando como as outras variáveis influenciam na variável "IsBestSeller"', RC3)
    ]

def RC1():
    PlotJustifyText("Nesta seção, exploramos a relação entre os autores e as avaliações atribuídas às suas obras. O objetivo é investigar se é possível inferir a avaliação de um livro com base no autor que o escreveu. Analisamos se a reputação ou estilo característico de cada autor influencia significativamente a percepção dos leitores, refletida nas avaliações recebidas.")
    PlotJustifyText('R^2: 0.8386 MSE: 0.0896')
    PlotJustifyText("O modelo mostrou-se eficaz na predição das avaliações dos livros, explicando 83,86% da variância (R2) e apresentando um erro quadrático médio (MSE) de 0,0896. Esses resultados indicam que o modelo consegue prever as avaliações com precisão, justificando sua adequação para este tipo de análise.")

def RC2():
    PlotJustifyText("Para inferir se um livro terá uma avaliação alta (4 ou mais estrelas), treinamos um modelo de classificação usando variáveis como preço, número de avaliações, editora e categoria. Inicialmente tratamos e dividimos os dados em conjuntos de treino e teste e, na sequência, ajustamos o modelo com Random Forest.")

    PlotJustifyText(f'Accuracy: 0.9487')
    PlotMarkdown(f"### Classification Report")
    PlotImage('RC2_1.png')

    PlotJustifyText("O modelo de Random Forest alcançou uma alta acurácia de 94%, indicando um bom desempenho geral. No entanto, ao analisar as métricas detalhadas, percebe-se que o modelo tem um desempenho significativamente melhor em prever avaliações altas (classe 1) com uma precisão de 96% e recall de 99%, enquanto o desempenho na classe de avaliações baixas (classe 0) é limitado, com uma precisão de 51% e recall de 24%. Isso sugere um desequilíbrio na capacidade do modelo de prever diferentes classes, possivelmente devido a um desbalanceamento nos dados.")
    
    PlotJustifyText("Para fins de comparação, o modelo KNN será testado com o mesmo conjunto de dados e, na sequência, ajustado para um K de 5. O resultado final é mostrado na tabela abaixo:")

    PlotJustifyText(f'Accuracy: 0.9518')
    PlotMarkdown(f"### Classification Report")
    PlotImage('RC2_2.png')

    PlotJustifyText("O modelo KNN possui um desempenho semelhante ao Random Forest, mas a classe das avaliações baixas (0) é cerca de 20% mais preciso. Isso ocorre porque modelos mais simples, como o KNN, funcionam melhor em casos de baixa dimensionalidade")

def RC3():
    PlotJustifyText("Nesta seção iremos tentar guiar nossas regressões e previsões. Para isso, primeiramente, como a grande maioria das colunas é categórica, faremos o OneHot Method, e então, usando algoritmos, iremos ter nosso relatório das variáveis que influenciam ou não a variável independente. Com isso, poderemos guiar melhor nossas análise.")
    PlotJustifyText('Estamos fazendo uma análise para entender quais fatores influenciam se um livro se torna um Best Seller na Amazon. Primeiro, transformamos as informações categóricas, como editoras e categorias de livros, em um formato que o modelo de computador possa entender. Depois, preparamos os dados, ajustando para que eles fiquem numa escala similar, o que ajuda o modelo a funcionar melhor.')
    PlotJustifyText('Em seguida, usamos um modelo matemático que tenta prever se um livro será Best Seller ou não, baseado nesses fatores. Para garantir que o modelo seja confiável, usamos uma técnica chamada validação cruzada, que divide os dados em partes e testa o modelo várias vezes. No final, verificamos quão preciso o modelo é em prever corretamente se um livro será Best Seller.')
    
    PlotJustifyText('Acurácias em cada fold: [0.98411029 0.98324631 0.98238167 0.9822314  0.9838843 ]')
    PlotJustifyText('Acurácia média: 0.9831707937145142')
    PlotJustifyText('Desvio padrão da acurácia: 0.0007619202305103511')
    
    PlotJustifyText("Aqui, estamos repetindo o processo de treinamento e teste do nosso modelo para garantir que ele seja preciso e confiável. Primeiramente, dividimos os dados em duas partes: uma parte para treinar o modelo e outra para testá-lo.")
    PlotJustifyText("Depois de treinar o modelo, verificamos o quão bem ele consegue prever se um livro será um Best Seller utilizando a parte de dados reservada para o teste.")
    PlotJustifyText("Esse processo é repetido várias vezes, com diferentes divisões dos dados, para garantir que os resultados não sejam apenas sorte. No final, calculamos a precisão média das previsões e quanto esses valores variam, o que nos ajuda a entender melhor o desempenho real do modelo.")
    
    PlotJustifyText("As acurácias em cada divisão foram as seguintes: [0.9832961859207132, 0.9831459267235982, 0.98369687711302, 0.9828203651298489, 0.9834965315168666, 0.9833462723197516, 0.9835215747163858, 0.9832961859207132, 0.9839473091082117, 0.9820941123437931].")
    PlotJustifyText("A acurácia média obtida foi de 0.9832661340812903, o que indica uma alta precisão do modelo em prever se um livro será Best Seller.")
    PlotJustifyText("O desvio padrão das acurácias foi de 0.00048609617942447695, o que mostra uma variação mínima entre as diferentes divisões, confirmando a consistência do modelo.")
    
    PlotJustifyText("Os resultados mostram as acurácias, ou seja, a precisão do modelo em prever corretamente se um livro será um Best Seller, em diferentes divisões dos dados.")
    PlotJustifyText("A acurácia para cada uma dessas divisões foi bem alta, variando de 98.2% a 98.4%, o que indica que o modelo é bastante confiável.")
    PlotJustifyText("Em média, o modelo tem uma precisão de aproximadamente 98.33%. A variação entre essas precisões foi muito pequena, com um desvio padrão de apenas 0.0486%, o que reforça a consistência do modelo em diferentes testes.")

    PlotJustifyText("Primeiro, extraímos os coeficientes do modelo de regressão logística para entender o impacto de cada variável nas previsões de Best Sellers. Cada coeficiente indica a influência de uma variável específica.")
    PlotJustifyText("Organizamos esses coeficientes para destacar as variáveis com maior impacto, tanto positivo quanto negativo. Depois, filtramos os coeficientes que são mais significativos, ou seja, aqueles que têm um valor acima de 0.2 ou abaixo de -0.2.")
    PlotJustifyText("Finalmente, criamos um gráfico de barras que mostra esses coeficientes filtrados, permitindo visualizar claramente quais variáveis têm a maior importância na determinação de um livro ser ou não um Best Seller.")
    
    PlotImage('RC3.png')
    
    PlotJustifyText("Com base na análise dos coeficientes do modelo, observamos que as variáveis 'KindleUnlimited', 'Sem Ficção' e 'Ciência e Matemática' têm uma influência significativa na probabilidade de um livro se tornar um Best Seller. Essas variáveis têm os coeficientes mais altos, indicando que são os fatores mais importantes para determinar se um livro será um Best Seller.")
    PlotJustifyText("Além disso, nosso modelo apresenta uma acurácia muito boa em todos os folds de teste, o que sugere que ele pode não estar generalizando bem para novos dados. Isso pode ser explicado pelo fato de que o conjunto de dados contém muito mais livros que não são Best Sellers do que aqueles que são, o que tende a inflar a acurácia geral. No entanto, o modelo é eficaz em identificar livros que não são Best Sellers.")
    
    PlotImage('RC3_1.png')
    
    PlotJustifyText("A matriz de confusão é uma ferramenta que ajuda a avaliar o desempenho do nosso modelo de classificação. Ela mostra o número de previsões corretas e incorretas feitas pelo modelo para cada classe. No gráfico, temos duas classes: 'Não Best-Seller' e 'Best-Seller'.")
    PlotJustifyText("Cada célula na matriz representa a contagem de instâncias para cada combinação de rótulo real e previsão do modelo. Os valores na diagonal principal (da esquerda para a direita) indicam o número de previsões corretas, enquanto os valores fora da diagonal representam previsões incorretas. A matriz de confusão nos ajuda a entender melhor onde o modelo está acertando e errando.")
    
    PlotImage('RC3_2.png')
    
    PlotJustifyText("Portanto, a Matriz de Confusão comprova que nosso modelo tem um desempenho geral bom, com a área sob a curva indicando uma boa taxa de acerto. No entanto, a matriz revela que o modelo está gerando muitos falsos positivos, classificando incorretamente livros que não são Best-Sellers como se fossem. Isso sugere que, embora o modelo tenha uma boa precisão geral, ele pode não estar capturando adequadamente a verdadeira taxa de Best-Sellers. Assim, pode ser interessante explorar outros modelos para avaliar e melhorar a eficácia das previsões.")

    
    PlotJustifyText('Acurácia: 0.9716010117452606')





    PlotJustifyText("O modelo mostrou-se eficaz na predição das avaliações dos livros, explicando 83,86% da variância (R2) e apresentando um erro quadrático médio (MSE) de 0,0896. Esses resultados indicam que o modelo consegue prever as avaliações com precisão, justificando sua adequação para este tipo de análise.")