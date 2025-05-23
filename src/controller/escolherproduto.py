from src.dao.produtodao import *
from ..controller.escolhercategoria import categoria_produto
from ..controller.escolherfornecedor import fornecedor_produto
from time import sleep
                
def mostrar_produtos():
    produtos = ProdutoDAO.listar()
    print("Produtos disponíveis:")
    sleep(0.5)
    for produto in produtos:
        print(f"ID: {produto.id_produto} - Nome: {produto.nome} - Preço: {produto.preco} - Categoria: {categoria_produto(produto.categoria.id_categoria)} - Fornecedor: {fornecedor_produto(produto.fornecedor.id_fornecedor)}")        
        sleep(0.3)
                
def escolher_produto():
    mostrar_produtos()
    produtos = ProdutoDAO.listar()
    escolha = input("Escolha um produto: ")
    
    for produto in produtos:
        if escolha.isdigit() and int(escolha) == produto.id_produto:
            return produto

        elif escolha.lower() == produto.nome.lower():
            print("Digite o ID do produto.")
        
    print("Produto não encontrada.")
    return None