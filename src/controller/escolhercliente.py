from src.dao.pessoadao import ClienteDAO
from time import sleep

def mostrar_clientes():
    clientes = ClienteDAO.listar()
    print("Clientes disponíveis:")
    sleep(0.5)
    for cliente in clientes:
        print(f"Nome: {cliente.nome} - Idade: {cliente.idade} - ID: {cliente.id_cliente}")
        sleep(0.3)
    