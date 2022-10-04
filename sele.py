from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
# passo 1: pegar a cotação do dólar
#abrir o navegador
navegador = webdriver.Chrome()
#entrar no google

navegador.get('https://www.google.com/webhp?hl=pt-BR&sa=X&ved=0ahUKEwjwgNXf85v5AhUWp5UCHVSBCG4QPAgI')

#pesquisar a cotaçaodolar no google
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação dólar')

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
#pegar a cotaçao
cotacao_dolar = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(cotacao_dolar)

navegador.get('https://www.google.com/webhp?hl=pt-BR&sa=X&ved=0ahUKEwjwgNXf85v5AhUWp5UCHVSBCG4QPAgI')

#pesquisar a cotaçaodolar no google
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação euro')

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
#pegar a cotaçao
cotacao_euro = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(cotacao_euro)

navegador.get('https://www.melhorcambio.com/ouro-hoje#:~:text=O%20valor%20do%20grama%20do,em%20R%24%20293%2C35.')#.send_keys(Keys.ENTER)
#pegar a cotaçao
cotacao_ouro = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
#exibir cotação
cotacao_ouro = cotacao_ouro.replace(',', '.')
print(cotacao_ouro)

# passo 4: atualizar a base de dados
tabela = pd.read_excel('Produtos.xlsx')
print(tabela)
# passo 5: recalcular os preços
# passo 6: exportar a base de dados
