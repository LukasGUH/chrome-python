#passo 2: entendimento da areaEmpressa
#passo 3: extraçãoObtenção de dados
#passo 4: ajuste de dados (tratamento limpeza)
#passo 5: analise exploratoria
#passo 6: modelagem + algoritimos( aqui que entra a inteligencia artificial, se necessario)
#passo 7: interpretação de resultados

#importar base de dados
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

tabela = pd.read_csv('advertising.csv')

#analise exploratótia

print(tabela.corr())

#criar o grafico
sns.heatmap(tabela.corr(), cmap='Wistia', annot=True)

#exibir o grafico
plt.show()

y = tabela['Vendas']
x = tabela[['TV, Radio, Jornal']]

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y test_size=0.3, random_state=1)

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

modelo_reressaolinear = LinearRegression
modelo_arvoredecisao = RandomForestRegressor

modelo_reressaolinear.fit(x_treino, y_treino)
modelo_arvoredecisao.fit(x_treino, y_treino)

RandomForestRegressor()
