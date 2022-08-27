#import pyautogui as pyg
#import time
#import pandas as pd

#time.sleep(5)

 
#while True:

#tabela = pd.read_excel(r'C:\Users\lukas\Downloads\Vendas - Dez.xlsx')
#print(tabela)

#3print(pyg.position()) 
import pandas as pd

tabela = pd.read_excel(r'C:\Users\lukas\Downloads\Vendas - Dez.xlsx')

quantidade = tabela['Quantidade']

faturamento = tabela['Valor Final'].sum()

print(faturamento)
