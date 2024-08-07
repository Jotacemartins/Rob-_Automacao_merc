import pyautogui
import time
import tkinter as tk
from tkinter import filedialog, messagebox

def selecionar_arquivo():
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione o arquivo TXT",
        filetypes=(("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*"))
    )
    return caminho_arquivo

def type_with_delay(text, delay=0.1):
    for char in text:
        pyautogui.typewrite(char, interval=delay)

def processar_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r') as file:
        for line in file:
            valores = line.strip().split(',')
            if len(valores) == 3:
                nome, cpf, cartao = valores
                time.sleep(1)
                pyautogui.click(742, 339, duration=0.5)
                type_with_delay(cpf, delay=0.1)
                pyautogui.click(718, 440, duration=0.5)
                pyautogui.write(cartao)
                pyautogui.click(765, 509, duration=1)
                pyautogui.click(769, 475, duration=3)
                pyautogui.doubleClick(519, 174, duration=6)
                time.sleep(1)
                pyautogui.hotkey('ctrl', 'shift', 's')
                time.sleep(1)
                pyautogui.click(683, 486, duration=2.0)
                pyautogui.click(715, 538, duration=2.0)
                pyautogui.click(487, 41, duration=1)
                pyautogui.click(536, 206, duration=2.0)
                pyautogui.click(742, 339, duration=0.5)
                pyautogui.hotkey('ctrl', 'a')
                pyautogui.press('backspace')
                pyautogui.click(718, 440, duration=0.5)
                pyautogui.hotkey('ctrl', 'a')
                pyautogui.press('backspace')
                time.sleep(1)
            else:
                continue

def iniciar_processamento():
    caminho_arquivo = entry_arquivo.get()
    if caminho_arquivo:
        try:
            processar_arquivo(caminho_arquivo)
            messagebox.showinfo("Sucesso", "Processamento concluído com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")
    else:
        messagebox.showwarning("Aviso", "Por favor, selecione um arquivo primeiro.")

def selecionar_arquivo_dialogo():
    caminho_arquivo = selecionar_arquivo()
    if caminho_arquivo:
        entry_arquivo.delete(0, tk.END)
        entry_arquivo.insert(0, caminho_arquivo)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Olá Amós, bom dia!")
    root.geometry("500x200")

    label_instrucao = tk.Label(root, text="Selecione o arquivo TXT e clique em 'Iniciar Processamento':")
    label_instrucao.pack(pady=10)

    frame_selecao = tk.Frame(root)
    frame_selecao.pack(pady=10)

    entry_arquivo = tk.Entry(frame_selecao, width=50)
    entry_arquivo.pack(side=tk.LEFT, padx=5)

    button_selecionar = tk.Button(frame_selecao, text="Selecionar Arquivo", command=selecionar_arquivo_dialogo)
    button_selecionar.pack(side=tk.LEFT)

    button_iniciar = tk.Button(root, text="Iniciar Processamento", command=iniciar_processamento)
    button_iniciar.pack(pady=20)

    root.mainloop()
