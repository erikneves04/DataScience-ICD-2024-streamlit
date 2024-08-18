from utils import PlotJustifyText, PlotImage

def Topics():
    return [
        ('Preços x Avaliações', AE1),
        ('Autores x Avaliações', AE2),
        ('Best Seller x Avaliações', AE3),
        ('Distribuição dos lançamentos', AE4),
        ('Distribuição dos preços', AE5),
        ('Relação de IsBestSeller com preço', AE6),
        ('Relação da Categoria e IsBestSeller', AE7),
        ('Relação de IsKindleUnlimited e IsBestSeller', AE8),
        ('Categoria mais vendida por Ano', AE9)
    ]

def AE1():
    PlotJustifyText("Nesse tópico buscamos avaliar se existe uma relação entre o preço de um livro e suas avaliação média. Para realizar essa análise vamos nos basear na média de preços e em um arredondamento das avaliações(que serão agrupadas de 0 a 5 e com seus decimais intermediários -- 0.5). Além disso serão exibidos dois cenários, um com os dados originais e outro com 95% dos dados, visando reduzir a influência de dados extremos e fora do normal(outliers) na visualização.")    
    PlotImage('AE1.png')
    PlotJustifyText("De acordo com os gráficos acima não temos nenhuma indicação de que exista uma relação entre essas duas variáveis, sendo assim, será necessário partir para uma segunda análise. Na segunda etapa, que será abordada em outro notebook, buscamos quebrar a associação entre preço e avaliação aplicando um teste de permutação em amostras reduzidas dos dados.")

def AE2():
    PlotJustifyText("Neste tópico buscamos avaliar se existe uma relação entre o número de publicações de um autor e sua avaliação média. Para realizar essa análise, vamos nos basear na média do número de publicações e em um arredondamento das avaliações que fizemos anteriormente.")
    PlotImage('AE2.png')
    PlotJustifyText("Esse resultado pode ser explicado pelo fato de que avaliações no geral tendem a ser boas, refletindo uma tendência positiva dos leitores ao avaliar livros. Além disso, novos autores com poucas publicações podem lançar obras de alta qualidade que recebem grande apreciação do público, ou podem ter uma base de leitores inicial que é particularmente entusiasta e generosa nas avaliações.")
    
def AE3():
    PlotImage('AE3.png')
    PlotJustifyText('Média das Estrelas dos Best Sellers: 4.49')    
    PlotJustifyText("Com base no gráfico e na estatística observada, livros que são Best Seller tem entre 4 e 5 estrelas, com média de aproximadamente 4,5 estrelas. Isso não é estranho, visto que a próprio conceito de 'BestSeller' carrega essa característica de ter uma avaliação boa, de modo geral.")

def AE4():
   PlotImage('AE4.png')

def AE5():     
    PlotImage('AE5.png')
    PlotJustifyText("A análise dos histogramas revela que a maior parte dos livros tem preços concentrados entre 0 e 20 dólares. Essa concentração sugere que a faixa de preço mais acessível é bastante popular entre os consumidores, possivelmente devido à sua atratividade financeira e à acessibilidade para um público mais amplo. Essa concentração pode refletir estratégias de precificação adotadas por editores e autores para alcançar um público maior e maximizar as vendas.")

def AE6():
    PlotJustifyText("Nesse tópico buscamos avaliar se existe uma relação entre o preço de um livro e se ele foi Best Seller. Para realizar essa análise vamos nos basear em faixas de preços e verificar em qual faixa se concentra mais os livros que foram Best Seller.")
    
    PlotJustifyText('O preço máximo é: R$ 682.0')
    PlotJustifyText('O preço mínimo é: R$ 000.0')
    PlotImage('AE6.png')
    
    PlotJustifyText("Analisando o Gráfico anterior, a faixa de preço predominantemente com livros Best Sellers é de 0 a 50 reais. Provavelmente, isso não é explicado pelo acaso, visto que a faixa de preço é relativamente baixa, o que pode gerar mais vendas, mas será bom testar para ver se a relação com o acaso ou não.Além disso, com o histograma, verificamos que os livros que custam 5 reais são os mais vendidos.")
    
def AE7():
    PlotJustifyText("Nesse tópico buscamos avaliar se existe uma relação entre a Categoria de um livro e Best Seller, para ver quais categorias com mais Best Sellers. Para realizar essa análise vamos verificar em qual categoria se concentra mais os livros que foram Best Seller.")
    PlotImage('AE7.png')
    PlotJustifyText("Nessa parte, as 3 principais categorias são 'Literature & Fiction', 'Science & Math' e 'Children's eBooks'. Literatura e Ficção pode ser explicado por ser um gênero que alcança todas as faixas etárias de idade. Matemática e Ciência geraram pesquisas no Google, as quais nos levaram a crer que esse genêro está no TOP 2 por ser livro que aborda aspectos da ciência de forma literária, como o livro Technology and Society: A Critical Analysis of 'The Coming Wave', que fala sobre as oportunidades e desafios trazidos pela Era Moderna. Esse tópico é interessante por si só, por trazer conhecimento de diversas formas, que não seja acadêmico. Livros para criança também é fácil de gerar uma hipotese, visto que a população mundial de crianças chega a 1/4 da população mundial total. Após essa pequena análise, vamos focar nos testes para ver se o acaso explica isso. Caso acaso não explique, nossa teoria pode estar certa.")

def AE8():
    PlotJustifyText("Nesse tópico buscamos entender se existe uma relação entre ser Best Seller e Kindle Unlimited. Para analisar agregaremos todos os Best Sellers e checar a frequência que pertence ao Kindle Unlimited.")
    PlotImage('AE8.png')
    PlotJustifyText("A observação de que a maioria dos livros Best Seller é Kindle Unlimited sugere uma possível influência do programa Kindle Unlimited (KU) nos rankings de best sellers da Amazon. Isso pode indicar que o algoritmo da Amazon favorece ou dá maior visibilidade a livros que fazem parte desse programa.")

def AE9():
    PlotImage('AE9.png')
    PlotJustifyText("No início dos anos 2000, a categoria 'Computers & Technology' liderou as vendas, refletindo o boom da tecnologia e o crescente interesse público nesse setor. A partir de 2017, os livros da categoria 'Law' dominaram o mercado, apesar dos elevados preços, que variam entre cerca de 45 a 60 dólares. Esse volume pode ser atribuído à legislações que obrigam instituições a adquirirem livros sobre temas como impostos e governança à medida que novas leis são implementadas.")