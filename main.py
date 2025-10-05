# main.py

Clientes = {
    'ana': {'senha': '1234', 'saldo': 1000},
    'joao': {'senha': 'abcd', 'saldo': 500},
    'maria': {'senha': 'senha123', 'saldo': 750},
    'pedro': {'senha': 'senha456', 'saldo': 300},
    'luana': {'senha': 'luana123', 'saldo': 5000},
    'carla': {'senha': 'carla456', 'saldo': 2000},
    'roberto': {'senha': 'roberto789', 'saldo': 1500}
}

def autenticar_usuario(nome, senha):
    if nome in Clientes and Clientes[nome]['senha'] == senha:
        return True
    return False

def ver_saldo(nome):
    return Clientes[nome]['saldo']

def depositar(nome, valor):
    if valor > 0:
        Clientes[nome]['saldo'] += valor
        return True
    return False

def sacar(nome, valor):
    if 0 < valor <= Clientes[nome]['saldo']:
        Clientes[nome]['saldo'] -= valor
        return True
    return False