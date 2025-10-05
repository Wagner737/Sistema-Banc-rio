# Interface.py
import tkinter as tk
from tkinter import messagebox
import main  # importa as funções e dados do main.py

usuario_atual = None

# -------------------------
# Funções da interface
# -------------------------
def login():
    global usuario_atual
    nome = entry_nome.get()
    senha = entry_senha.get()

    if main.autenticar_usuario(nome, senha):
        usuario_atual = nome
        messagebox.showinfo("Login", f"Bem-vindo, {nome}!")
        abrir_menu()
    else:
        messagebox.showerror("Erro", "Usuário ou senha inválidos.")

def ver_saldo():
    saldo = main.ver_saldo(usuario_atual)
    messagebox.showinfo("Saldo", f"Seu saldo é: R$ {saldo:.2f}")

def depositar():
    try:
        valor = float(entry_valor.get())
        if main.depositar(usuario_atual, valor):
            messagebox.showinfo("Depósito", f"Depósito de R$ {valor:.2f} realizado!\nNovo saldo: R$ {main.ver_saldo(usuario_atual):.2f}")
        else:
            messagebox.showwarning("Atenção", "Digite um valor válido.")
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido.")

def sacar():
    try:
        valor = float(entry_valor.get())
        if main.sacar(usuario_atual, valor):
            messagebox.showinfo("Saque", f"Saque de R$ {valor:.2f} realizado!\nNovo saldo: R$ {main.ver_saldo(usuario_atual):.2f}")
        else:
            messagebox.showwarning("Atenção", "Saldo insuficiente ou valor inválido.")
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido.")

# -------------------------
# Interface gráfica
# -------------------------
root = tk.Tk()
root.title("Banco Tkinter")
root.geometry("350x300")
root.configure(bg="#f0f0f0")

# Tela de login
frame_login = tk.Frame(root, bg="#f0f0f0")
frame_login.pack(pady=20)

tk.Label(frame_login, text="Usuário:", bg="#f0f0f0", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)
entry_nome = tk.Entry(frame_login, font=("Arial", 12))
entry_nome.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_login, text="Senha:", bg="#f0f0f0", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5)
entry_senha = tk.Entry(frame_login, show="*", font=("Arial", 12))
entry_senha.grid(row=1, column=1, padx=5, pady=5)

tk.Button(root, text="Entrar", command=login, bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=10)

# Campo de valor (usado em depósito/saque)
entry_valor = tk.Entry(root, font=("Arial", 12))
entry_valor.pack(pady=5)

def abrir_menu():
    menu = tk.Toplevel(root)
    menu.title("Menu Bancário")
    menu.geometry("300x250")
    menu.configure(bg="#e6f2ff")

    tk.Label(menu, text=f"Bem-vindo, {usuario_atual}!", font=("Arial", 14, "bold"), bg="#e6f2ff").pack(pady=10)

    tk.Button(menu, text="Ver Saldo", command=ver_saldo, width=20, bg="#2196F3", fg="white", font=("Arial", 12)).pack(pady=5)
    tk.Button(menu, text="Depositar", command=depositar, width=20, bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=5)
    tk.Button(menu, text="Sacar", command=sacar, width=20, bg="#f44336", fg="white", font=("Arial", 12)).pack(pady=5)
    tk.Button(menu, text="Sair", command=menu.destroy, width=20, bg="#9E9E9E", fg="white", font=("Arial", 12)).pack(pady=5)

root.mainloop()