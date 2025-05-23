from src.dao.produtodao import *
from time import sleep
                
def mostrar_fornecedores():
    fornecedores = FornecedorDAO.listar()
    print("Fornecedores disponíveis:")
    sleep(0.5)
    for fornecedor in fornecedores:
        print(f"ID: {fornecedor.id_fornecedor} - Nome: {fornecedor.nome}")
        sleep(0.3)          
                
def escolher_fornecedor():
    mostrar_fornecedores()
    fornecedores = FornecedorDAO.listar()
    escolha = input("Escolha um fornecedor: ")
    
    for fornecedor in fornecedores:
        if escolha.isdigit() and int(escolha) == fornecedor.id_fornecedor:
            return fornecedor

        elif escolha.lower() == fornecedor.nome.lower():
            print("Digite o ID do fornecedor.")
        
    print("Fornecedor não encontrada.")
    return None

def fornecedor_produto(valor):
    fornecedores = FornecedorDAO.listar()
    for fornecedor in fornecedores:
        if int(valor) == fornecedor.id_fornecedor:
            return fornecedor.nome