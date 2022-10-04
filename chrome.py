import pyautogui as pyg
import pyperclip
import time
import pandas as pd

pyg.PAUSE = 1

# passo 1 Entrar no sistema (no caso vai entrar no link)
pyg.press('win')
pyg.write('chrome')
pyg.press('enter')

pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing')
pyg.hotkey('ctrl', 'v')
pyg.press('enter')
#site carregando
time.sleep(5)
# passo 2 navegar no sistema e encontrar a base de dados(encontar na base exportar)
pyg.click(x=470, y=329, clicks= 2)
time.sleep(2)
# passo 3 download da base de dados
pyg.click(x=500, y=446)
pyg.click(x=1655, y=198)
pyg.click(x=1501, y=708)
time.sleep(7)
# passo 4 calcular os faturadores (faturamento e quantidades de produtos)
tabela = pd.read_excel(r'C:\Users\lukas\Downloads\Vendas - Dez.xlsx')

quantidade = tabela['Quantidade'].sum()

faturamento = tabela['Valor Final'].sum()

# passo 5 entar no email
pyg.hotkey('ctrl', 't')
pyperclip.copy('https://mail.google.com/mail/u/0/#inbox')
pyg.hotkey('ctrl', 'v')
pyg.press('enter')
time.sleep(7)

# passo 6 enviar email
pyg.click(x=37, y=222)
time.sleep(2)
pyg.write('gustavolukas62@gmail.com')
pyg.press('tab')
pyg.press('tab')

pyperclip.copy('Relatorio de Vendas')
pyg.hotkey('ctrl', 'v')
pyg.press('tab')

texto = f"""
Prezados, bom dia

O faturamento de ontem foi de: R${faturamento:,.2f}
A quantidade de produtos foi de: {quantidade:,}

Abs
Lucas G"""

pyperclip.copy(texto)
pyg.hotkey('ctrl', 'v')

pyg.hotkey('ctrl', 'enter')



