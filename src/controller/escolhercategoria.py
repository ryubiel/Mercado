from src.dao.produtodao import *
                
def mostrar_categorias():
    categorias = CategoriaDAO.listar()
    print("Categorias disponíveis:")
    for categoria in categorias:
        print(f"ID: {categoria.id_categoria} - Nome: {categoria.nome}")         
                
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