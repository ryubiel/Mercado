from src.dao.produtodao import CategoriaDAO
from time import sleep
                
def mostrar_categorias():
    categorias = CategoriaDAO.listar()
    print("Categorias disponíveis:")
    sleep(0.5)
    for categoria in categorias:
        print(f"ID: {categoria.id_categoria} - Nome: {categoria.nome}")
        sleep(0.3)         
                
def escolher_categoria():
    mostrar_categorias()
    categorias = CategoriaDAO.listar()
    escolha = input("Escolha uma categoria: ")
    
    for categoria in categorias:
        if escolha.isdigit() and int(escolha) == categoria.id_categoria:
            return categoria

        elif escolha.lower() == categoria.nome.lower():
            print("Digite o ID da categoria.")
        
    print("Categoria não encontrada.")
    return None

def categoria_produto(valor):
    categorias = CategoriaDAO.listar()
    for categoria in categorias:
        if int(valor) == categoria.id_categoria:
            return categoria.nome