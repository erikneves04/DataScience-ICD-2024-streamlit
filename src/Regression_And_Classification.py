from utils import PlotJustifyText, PlotGraph, LoadDatabases, PlotMarkdown

import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
import statsmodels.api as sm
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_curve, auc, roc_auc_score
from sklearn.model_selection import cross_val_score, KFold
import warnings
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier

sns.set_theme()
warnings.filterwarnings("ignore")

# Acessos aos dados
kindle_data, books = LoadDatabases()

def Topics():
    return [
       ('Autores e avaliações', RC1),
       ('Classificando Avaliações', RC2)
    ]

def RC1():
    global kindle_data
    PlotJustifyText("Nesta seção, exploramos a relação entre os autores e as avaliações atribuídas às suas obras. O objetivo é investigar se é possível inferir a avaliação de um livro com base no autor que o escreveu. Analisamos se a reputação ou estilo característico de cada autor influencia significativamente a percepção dos leitores, refletida nas avaliações recebidas.")
    
    autor_aval_media = kindle_data.groupby('Authors')['Stars'].mean().reset_index()
    autor_aval_media.columns = ['Authors', 'MeanStars']

    kindle_data = kindle_data.merge(autor_aval_media, on='Authors', how='left')

    X = kindle_data[['MeanStars']]
    y = kindle_data['Stars']

    # Divisão dos dados em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Treinamento
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Fazer previsões
    y_pred = model.predict(X_test)

    # Avaliação do modelo
    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)

    PlotJustifyText(f'R^2: {r2:.4f}\nMSE: {mse:.4f}')
    PlotJustifyText("O modelo mostrou-se eficaz na predição das avaliações dos livros, explicando 83,86% da variância (R2) e apresentando um erro quadrático médio (MSE) de 0,0896. Esses resultados indicam que o modelo consegue prever as avaliações com precisão, justificando sua adequação para este tipo de análise.")

def RC2():
    global kindle_data
    PlotJustifyText("Para inferir se um livro terá uma avaliação alta (4 ou mais estrelas), treinamos um modelo de classificação usando variáveis como preço, número de avaliações, editora e categoria. Inicialmente tratamos e dividimos os dados em conjuntos de treino e teste e, na sequência, ajustamos o modelo com Random Forest.")

    # 1. Definir do problema
    kindle_data['HighRating'] = (kindle_data['Stars'] >= 4).astype(int)

    # 2. Pré-processamento
    numeric_features = ['Reviews']
    categorical_features = ['Publisher', 'Category']

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numeric_features),
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)])

    # 3. Divisão dos Dados
    X = kindle_data[['Reviews', 'Publisher', 'Category']]
    y = kindle_data['HighRating']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 4. Treinamento de um Classificador
    clf = Pipeline(steps=[('preprocessor', preprocessor),
                        ('classifier', RandomForestClassifier(random_state=42))])

    clf.fit(X_train, y_train)

    # 5. Avaliação do Modelo
    y_pred = clf.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    PlotJustifyText(f'Accuracy: {accuracy:.4f}')
    
    # Exibir o relatório de classificação formatado
    PlotMarkdown(f"### Classification Report\n\n{report}")

    PlotJustifyText("O modelo de Random Forest alcançou uma alta acurácia de 94%, indicando um bom desempenho geral. No entanto, ao analisar as métricas detalhadas, percebe-se que o modelo tem um desempenho significativamente melhor em prever avaliações altas (classe 1) com uma precisão de 96% e recall de 99%, enquanto o desempenho na classe de avaliações baixas (classe 0) é limitado, com uma precisão de 51% e recall de 24%. Isso sugere um desequilíbrio na capacidade do modelo de prever diferentes classes, possivelmente devido a um desbalanceamento nos dados.")
    
    # Os mesmos dados serão utilizados no KNN

    PlotJustifyText("Para fins de comparação, o modelo KNN será testado com o mesmo conjunto de dados e, na sequência, ajustado para um K de 5. O resultado final é mostrado na tabela abaixo:")

    clf_2 = Pipeline(steps=[('preprocessor', preprocessor),
                        ('classifier', KNeighborsClassifier(n_neighbors=5))])
    
    clf_2.fit(X_train, y_train)
    
    y_pred_2 = clf_2.predict(X_test)

    accuracy_2 = accuracy_score(y_test, y_pred_2)

    report2 = classification_report(y_test, y_pred_2)

    PlotJustifyText(f'Accuracy: {accuracy_2:.4f}')

    PlotMarkdown(f"### Classification Report\n\n{report2}")

    PlotJustifyText("O modelo KNN possui um desempenho semelhante ao Random Forest, mas a classe das avaliações baixas (0) é cerca de 20% mais preciso. Isso ocorre porque modelos mais simples, como o KNN, funcionam melhor em casos de baixa dimensionalidade")

