from utils import PlotJustifyText, PlotMarkdown, PlotImage

def Topics():
    return [
       ('Autores e avaliações', RC1),
       ('Classificando Avaliações', RC2),
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