# Data Science Books Analysis

Este projeto utiliza o Streamlit para analisar e visualizar dados relacionados a livros de ciência de dados. O objetivo é identificar padrões e fatores que influenciam a popularidade dos livros, utilizando técnicas de análise de dados e modelagem preditiva.

## Funcionalidades

- **Visualização de Dados**: Gráficos interativos que exibem informações sobre preços, avaliações e outros atributos dos livros de ciência de dados.
- **Análise de Correlação**: Exploração da relação entre diferentes características dos livros, como preço, número de avaliações e pontuação média.
- **Modelagem Preditiva**: Uso de regressão logística e árvores de decisão para prever quais livros têm maior probabilidade de se tornarem Best Sellers.
- **Validação Cruzada**: Implementação de validação cruzada para avaliar a precisão dos modelos preditivos.
- **Intervalos de Confiança**: Cálculo e exibição de intervalos de confiança para as previsões realizadas pelos modelos.
- **Relatórios Interativos**: Interface amigável para visualizar os resultados da análise de forma interativa.

## Como Executar

Para executar o projeto localmente, siga as instruções abaixo:

1. **Clone o repositório**:

    ```bash
    git clone <URL_DO_REPOSITORIO>
    ```

2. **Navegue até o diretório do projeto**:

    ```bash
    cd datascience-books-analysis
    ```

3. **Instale as dependências**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Execute a aplicação Streamlit**:

    ```bash
    streamlit run app.py
    ```

## Estrutura do Projeto

- **app.py**: Arquivo principal que contém o código da aplicação Streamlit.
- **data/**: Diretório que contém os datasets utilizados na análise.
- **scripts/**: Scripts auxiliares para pré-processamento de dados e modelagem.
- **assets/**: Imagens e outros recursos estáticos utilizados na aplicação.
- **README.md**: Este arquivo, que fornece uma visão geral do projeto.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal utilizada no projeto.
- **Streamlit**: Framework para criação de aplicações web interativas em Python.
- **Pandas**: Biblioteca para manipulação e análise de dados.
- **Seaborn/Matplotlib**: Bibliotecas para visualização de dados.
- **Scikit-learn**: Biblioteca para modelagem preditiva e machine learning.

## Contribuindo

Contribuições são bem-vindas! Se você quiser melhorar este projeto, siga os passos abaixo:

1. **Faça um fork do repositório.**
2. **Crie uma nova branch**:

    ```bash
    git checkout -b feature/sua-feature
    ```

3. **Commit suas mudanças**:

    ```bash
    git commit -m 'Adiciona uma nova feature'
    ```

4. **Envie para a branch original**:

    ```bash
    git push origin feature/sua-feature
    ```

5. **Abra um pull request.**

## Licença

Este projeto é licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.
