from src.dao.produtodao import *
                
def mostrar_fornecedores():
    fornecedores = FornecedorDAO.listar()
    print("Fornecedores disponíveis:")
    for fornecedor in fornecedores:
        print(f"ID: {fornecedor.id_fornecedor} - Nome: {fornecedor.nome}")         
                
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