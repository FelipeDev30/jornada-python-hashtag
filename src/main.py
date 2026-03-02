# bibliotecas = pacotes de códigos prontos para serem usados
# pip install pyautogui
# Este módulo demonstra um script automatizado simples.
# Os comentários originais descreviam passos fictícios de cadastro de produtos.

# funções utilitárias e fluxo principal abaixo.

# Passo 1: Abrir o navegador e acessar o site de cadastro de produtos
# Passo 2: Preencher o formulário de cadastro com os detalhes do produto
# Passo 3: Submeter o formulário e verificar se o produto foi cadastrado com sucesso
# Passo 4: Repetir o processo para múltiplos produtos, se necessário
# Nota: Este é um exemplo fictício e não interage com um site real.


import pyautogui
import time
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.PAUSE = 0.5

pyautogui.press('win')

pyautogui.write('chrome')

pyautogui.press('enter')

pyautogui.write(link)

pyautogui.press('enter')
time.sleep(3)
pyautogui.press('tab')
pyautogui.write('admin')
pyautogui.press('tab')
pyautogui.write('admin@2025@#520#')
pyautogui.press('enter')
pyautogui.click(x=3813, y=734)


