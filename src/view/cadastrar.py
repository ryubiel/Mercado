from ..model.pessoa import *
from ..model.produto import *
from ..dao.pessoadao import *
from ..dao.produtodao import *
from ..controller.id import gerar_id
from ..controller.escolhercategoria import escolher_categoria
from ..controller.escolherfornecedor import escolher_fornecedor
from time import sleep

def view_cadastrar():
    while True:
        cadastrar = int(input("O que deseja cadastrar \n1 - cliente\n2 - funcionário \n3 - Categoria \n4 - Fornecedor \n5 - Produto \n9 - Voltar \nEscolha uma opção: "))
        sleep(1)
        if cadastrar in [1, 2, 3, 4, 5]:
            if cadastrar in [1, 2]:
                nome = input("Digite o nome: ")
                idade = int(input("Digite a idade: "))
                if cadastrar == 1:
                    id_cliente = gerar_id(cliente=True)
                    cliente = Cliente(nome, idade, id_cliente)
                    ClienteDAO.inserir(cliente)
                elif cadastrar == 2:
                    cargo = input("Digite o cargo: ")
                    id_func = gerar_id(funcionario=True)
                    salario = float(input("Digite o salário: "))
                    funcionario = Funcionario(nome, idade, cargo, id_func, salario)
                    FuncionarioDAO.inserir(funcionario)       
            elif cadastrar == 3:
                nome_categoria = input("Digite o nome da categoria: ")
                id_categoria = gerar_id(categoria=True)
                categoria = Categoria(id_categoria, nome_categoria)
                CategoriaDAO.inserir(categoria)
            elif cadastrar == 4:
                nome_fornecedor = input("Digite o nome do fornecedor: ")
                cnpj = input("Digite o CNPJ do fornecedor: ")
                id_fornecedor = gerar_id(fornecedor=True)
                fornecedor = Fornecedor(id_fornecedor, nome_fornecedor, cnpj)
                FornecedorDAO.inserir(fornecedor)
            elif cadastrar == 5:
                nome_produto = input("Digite o nome do produto: ")
                preco = float(input("Digite o preço do produto: "))
                id_produto = gerar_id(produto=True)
                categoria = escolher_categoria()
                fornecedor = escolher_fornecedor()
                produto = Produto(id_produto, nome_produto, preco, categoria, fornecedor)
                ProdutoDAO.inserir(produto)
        elif cadastrar == 9:
            break
        else:
            print("Opção inválida. Tente novamente.")