from utils import PlotJustifyText, PlotMarkdown, PlotImage

def Topics():
    return [
       ('Classificando Avaliações', C1),
    ]

def C1():
    PlotJustifyText('Para inferir se um livro terá uma avaliação alta (4 ou mais estrelas), treinamos um modelo de classificação usando variáveis como preço, número de avaliações, editora e categoria. Inicialmente tratamos e dividimos os dados em conjuntos de treino e teste e, na sequência, ajustamos o modelo com Random Forest.')
    
    PlotJustifyText('Acurácia do modelo: 0.9487')
    PlotImage('C1_1.png')

    PlotJustifyText('O modelo de Random Forest alcançou uma alta acurácia de 94%, indicando um bom desempenho geral. No entanto, ao analisar as métricas detalhadas, percebe-se que o modelo tem um desempenho significativamente melhor em prever avaliações altas (classe 1) com uma precisão de 96% e recall de 99%, enquanto o desempenho na classe de avaliações baixas (classe 0) é limitado, com uma precisão de 51% e recall de 24%. Isso sugere um desequilíbrio na capacidade do modelo de prever diferentes classes, possivelmente devido a um desbalanceamento nos dados.')

    PlotJustifyText('Acurácia do modelo: 0.9520')
    PlotImage('C1_2.png')

    PlotJustifyText('Para fins de comparação, o mesmo conjunto de teste e treino foi usado com o modelo K-nearest Neighbors (KNN). Os resultados foram consistentes em apresentar uma precisão semelhante nos casos de avaliação alta (1), com altas métricas de precisão, recall e F1-score, enquanto o KNN tem um resultado ligeiramente melhor na classe das avaliações baixas (0), com valores de precisão maiores que o Random Forest')
