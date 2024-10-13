import keyboard
import pyautogui
from time import sleep
import sys
import os
import logging

# Configuração de logs
logging.basicConfig(
    filename='app.log',  # Nome do arquivo de log
    level=logging.INFO,  # Nível de log (INFO, DEBUG, ERROR)
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Função para obter o caminho da imagem embutida ou local
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

imagem = resource_path('image.png')  # Localiza a imagem

def minha_funcao():
    try:
        logging.info("Iniciando função com clique em (222, 109)")
        pyautogui.click(x=222, y=109, button='right')
        sleep(0.3)

        localizacao = pyautogui.locateCenterOnScreen(imagem)

        if localizacao is not None:
            logging.info(f"Imagem encontrada em {localizacao}")
            pyautogui.click(localizacao)
        else:
            logging.warning("Imagem não encontrada na tela.")
            print("Imagem não encontrada na tela.")

    except pyautogui.ImageNotFoundException:
        logging.error("Erro: A imagem não foi encontrada.")
        print("Erro: A imagem não foi encontrada.")
    except Exception as e:
        logging.exception(f"Ocorreu um erro inesperado: {e}")
        print(f"Ocorreu um erro inesperado: {e}")

logging.info("Aplicação iniciada. Pressione '0' para executar a função.")
keyboard.add_hotkey('0', minha_funcao)  # Tecla '0' para executar
keyboard.wait('esc')  # Aguarda 'ESC' para encerrar
