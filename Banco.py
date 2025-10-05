import tkinter as tk
from tkinter import messagebox

# -------------------------
# Dados dos clientes
# -------------------------
Clientes = {
    'ana': {'senha': '1234', 'saldo': 1000},
    'joao': {'senha': 'abcd', 'saldo': 500},
    'maria': {'senha': 'senha123', 'saldo': 750},
    'pedro': {'senha': 'senha456', 'saldo': 300},
    'luana': {'senha': 'luana123', 'saldo': 5000},
    'carla': {'senha': 'carla456', 'saldo': 2000},
    'roberto': {'senha': 'roberto789', 'saldo': 1500}
}

usuario_atual = None  # guarda o cliente logado

# -------------------------
# Funções do sistema
# -------------------------
def login():
    global usuario_atual
    nome = entry_nome.get()
    senha = entry_senha.get()

    if nome in Clientes and Clientes[nome]['senha'] == senha:
        usuario_atual = nome
        messagebox.showinfo("Login", f"Bem-vindo, {nome}!")
        abrir_menu()
    else:
        messagebox.showerror("Erro", "Usuário ou senha inválidos.")

def ver_saldo():
    saldo = Clientes[usuario_atual]['saldo']
    messagebox.showinfo("Saldo", f"Seu saldo é: R$ {saldo:.2f}")

def depositar():
    valor = entry_valor.get()
    try:
        valor = float(valor)
        if valor > 0:
            Clientes[usuario_atual]['saldo'] += valor
            messagebox.showinfo("Depósito", f"Depósito de R$ {valor:.2f} realizado!\nNovo saldo: R$ {Clientes[usuario_atual]['saldo']:.2f}")
        else:
            messagebox.showwarning("Atenção", "Digite um valor válido.")
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido.")

def sacar():
    valor = entry_valor.get()
    try:
        valor = float(valor)
        if 0 < valor <= Clientes[usuario_atual]['saldo']:
            Clientes[usuario_atual]['saldo'] -= valor
            messagebox.showinfo("Saque", f"Saque de R$ {valor:.2f} realizado!\nNovo saldo: R$ {Clientes[usuario_atual]['saldo']:.2f}")
        else:
            messagebox.showwarning("Atenção", "Saldo insuficiente ou valor inválido.")
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido.")

# -------------------------
# Interface gráfica
# -------------------------
root = tk.Tk()
root.title("Banco Tkinter")
root.geometry("300x250")

# Tela de login
tk.Label(root, text="Usuário:").pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

tk.Label(root, text="Senha:").pack()
entry_senha = tk.Entry(root, show="*")
entry_senha.pack()

tk.Button(root, text="Entrar", command=login).pack(pady=10)

# Campo de valor (usado em depósito/saque)
entry_valor = tk.Entry(root)
entry_valor.pack(pady=5)

def abrir_menu():
    menu = tk.Toplevel(root)
    menu.title("Menu Bancário")
    menu.geometry("300x200")

    tk.Button(menu, text="Ver Saldo", command=ver_saldo).pack(pady=5)
    tk.Button(menu, text="Depositar", command=depositar).pack(pady=5)
    tk.Button(menu, text="Sacar", command=sacar).pack(pady=5)
    tk.Button(menu, text="Sair", command=menu.destroy).pack(pady=5)

root.mainloop()