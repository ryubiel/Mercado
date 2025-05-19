from ..dao.pessoadao import *
from ..dao.produtodao import *
from time import sleep


def view_verificar():
    while True:
        sleep(0.5)
        listar = int(input("O que deseja Verificar \n1 - cliente\n2 - funcionário\n3 - categorias \n4 - fornecedores \n5 - produtos \n9 - voltar \nEscolha uma opção: "))
        if listar in [1 , 2, 3, 4, 5]:
            if listar == 1:
                clientes = ClienteDAO.listar()
                sleep(0.5)
                for cliente in clientes:
                    print(f"Nome: {cliente.nome} - Idade: {cliente.idade} - ID: {cliente.id_cliente}")
                    sleep(0.3)
                sleep(1)
            elif listar == 2:
                funcionarios = FuncionarioDAO.listar()
                sleep(0.5)
                for funcionario in funcionarios:
                    print(f"Nome: {funcionario.nome} - Idade: {funcionario.idade} - Cargo: {funcionario.cargo} - ID: {funcionario.id_func} - Salário: {funcionario.salario}")
                    sleep(0.3)
            elif listar == 3:
                categorias = CategoriaDAO.listar()
                sleep(0.5)
                for categoria in categorias:
                    print(f"ID: {categoria.id_categoria} - Nome: {categoria.nome}")
                    sleep(0.3)
            elif listar == 4:
                fornecedores = FornecedorDAO.listar()
                sleep(0.5)
                for fornecedor in fornecedores:
                    print(f"ID: {fornecedor.id_fornecedor} - Nome: {fornecedor.nome} - CNPJ: {fornecedor.cnpj}")
                    sleep(0.3)
            elif listar == 5:
                produtos = ProdutoDAO.listar()
                sleep(0.5)
                for produto in produtos:
                    print(f"ID: {produto.id_produto} - Nome: {produto.nome} - Preço: {produto.preco} - Categoria: {produto.categoria.nome} - Fornecedor: {produto.fornecedor.nome}")
                    sleep(0.3)
        elif listar == 9:
            break
        else:
            print("Opção inválida. Tente novamente.\n" + ("-" * 35))