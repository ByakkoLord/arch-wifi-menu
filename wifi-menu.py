import subprocess
import tkinter as tk
from tkinter import simpledialog, messagebox

# Exibe as redes Wi-Fi disponíveis
def showNetworks():
    result = subprocess.run(["nmcli", "-t", "-f", "SSID,SIGNAL", "dev", "wifi"], capture_output=True, text=True)
    print("Saída1:", result.stdout)
    print("Erros1:", result.stderr)

# Conecta-se à rede Wi-Fi especificada com a senha fornecida
def connectNetwork():
    result2 = subprocess.run(["nmcli", "dev", "wifi", "connect", "2GEDILTON", "--ask"], capture_output=True, text=True)
    print("Saída2:", result2.stdout)
    print("Erros2:", result2.stderr)

# Criando a interface
root = tk.Tk()
root.title("Gerenciador de Wi-Fi")
root.geometry("400x300")

# Botão para listar redes
btn_listar = tk.Button(root, text="Listar Redes", command=showNetworks())
btn_listar.pack(pady=10)

# Lista de redes
lista_redes = tk.Listbox(root, height=10)
lista_redes.pack(pady=10, fill=tk.BOTH, expand=True)

# Botão para conectar
btn_conectar = tk.Button(root, text="Conectar", command=connectNetwork())
btn_conectar.pack(pady=10)

root.mainloop()