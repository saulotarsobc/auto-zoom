import keyboard
import pyautogui
from time import sleep
import sys
import os
import logging
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from threading import Thread

# Função para obter o caminho da imagem embutida ou local
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

imagem = resource_path('image.png')  # Localiza a imagem

# Configuração da janela de logs
root = tk.Tk()
root.title("Logs do Programa")
root.geometry("600x400")

# Área de texto com barra de rolagem para exibir os logs
text_area = ScrolledText(root, state='disabled', wrap='word', font=('Consolas', 10))
text_area.pack(expand=True, fill='both')

# Configuração dos logs
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Função para exibir as mensagens de log na janela
def log_to_window(message):
    text_area.config(state='normal')
    text_area.insert(tk.END, message + '\n')
    text_area.see(tk.END)  # Rola para a última linha
    text_area.config(state='disabled')

# Handler personalizado para redirecionar logs para a janela
class TextHandler(logging.Handler):
    def emit(self, record):
        log_to_window(self.format(record))

# Adiciona o handler personalizado ao logger
handler = TextHandler()
logging.getLogger().addHandler(handler)

# Função que será chamada pela hotkey '0'
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
    except Exception as e:
        logging.exception(f"Ocorreu um erro inesperado: {e}")

# Função para executar `minha_funcao()` em uma thread separada
def run_in_thread():
    thread = Thread(target=minha_funcao)
    thread.start()

logging.info("Aplicação iniciada. Pressione '0' para executar a função.")
keyboard.add_hotkey('0', run_in_thread)  # Executa a função na thread ao pressionar '0'

# Verifica a tecla ESC em uma thread separada para não bloquear a interface
def monitorar_esc():
    keyboard.wait('esc')
    root.quit()

Thread(target=monitorar_esc).start()  # Inicia a monitorização do ESC em segundo plano

root.mainloop()
