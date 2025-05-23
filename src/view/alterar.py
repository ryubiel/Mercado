from ..controller.escolhercliente import mostrar_clientes
from ..controller.escolherfuncionario import mostrar_funcionarios
from ..controller.escolhercategoria import mostrar_categorias
from ..controller.escolherfornecedor import mostrar_fornecedores
from ..controller.escolherproduto import mostrar_produtos
from ..dao.pessoadao import *
from ..dao.produtodao import *

def view_alterar():
    while True:
        alterar = int(input("O que deseja alterar \n1 - cliente\n2 - funcionário\n3 - categorias \n4 - fornecedores \n5 - produtos \n9 - voltar \nEscolha uma opção: "))
        if alterar in [1, 2, 3, 4, 5]:
            if alterar == 1:
                mostrar_clientes()
                id_cliente = int(input("Digite o ID do cliente que deseja alterar: "))
                clientes = ClienteDAO.listar()
                
                for cliente in clientes:
                    if cliente.id_cliente == int(id_cliente):
                        dado = int(input("Qual dado deseja alterar? \n1 - Nome\n2 - Idade\nEscolha uma opção: "))
                        if dado == 1:
                            novo_nome = input("Digite o novo nome: ")
                            ClienteDAO.alterar_nome(cliente.id_cliente, novo_nome)
                            print(f"Nome do cliente {cliente.nome} alterado para {novo_nome}.")
                        elif dado == 2:
                            nova_idade = int(input("Digite a nova idade: "))
                            ClienteDAO.alterar_idade(cliente.id_cliente, nova_idade)
                            print(f"Idade do cliente {cliente.idade} alterada para {nova_idade}.")
                        else:
                            print("Opção inválida. Tente novamente.")
                        break
                else:
                    print(f"Cliente com ID {id_cliente} não encontrado.")
                    
            elif alterar == 2:
                mostrar_funcionarios()
                id_funcionario = int(input("Digite o ID do funcionário que deseja alterar: "))
                funcionarios = FuncionarioDAO.listar()
                
                for funcionario in funcionarios:
                    if funcionario.id_func == int(id_funcionario):
                        dado = int(input("Qual dado deseja alterar? \n1 - Nome\n2 - Idade\n3 - Cargo\n4 - Salário\nEscolha uma opção: "))
                        if dado == 1:
                            novo_nome = input("Digite o novo nome: ")
                            FuncionarioDAO.alterar_nome(funcionario.id_func, novo_nome)
                            print(f"Nome do funcionário {funcionario.nome} alterado para {novo_nome}.")
                        elif dado == 2:
                            nova_idade = int(input("Digite a nova idade: "))
                            FuncionarioDAO.alterar_idade(funcionario.id_func, nova_idade)
                            print(f"Idade do funcionário {funcionario.id_func} alterada para {nova_idade}.")
                        elif dado == 3:
                            novo_cargo = input("Digite o novo cargo: ")
                            FuncionarioDAO.alterar_cargo(funcionario.id_func, novo_cargo)
                            print(f"Cargo do funcionário {funcionario.nome} alterado para {novo_cargo}.")
                        elif dado == 4:
                            novo_salario = float(input("Digite o novo salário: "))
                            FuncionarioDAO.alterar_salario(funcionario.id_func, novo_salario)
                            print(f"Salário do funcionário {funcionario.nome} alterado para {novo_salario}.")
                        else:
                            print("Opção inválida. Tente novamente.")
                        break
                else:
                    print(f"Funcionário com ID {id_funcionario} não encontrado.")
                
            elif alterar == 3:
                mostrar_categorias()
                id_categoria = int(input("Digite o ID da categoria que deseja alterar: "))
                categorias = CategoriaDAO.listar()
                for categoria in categorias:
                    if categoria.id_categoria == int(id_categoria):
                        novo_nome = input("Digite o novo nome da categoria: ")
                        CategoriaDAO.alterar_nome(categoria.id_categoria, novo_nome)
                        print(f"Nome da categoria {categoria.nome} alterado para {novo_nome}.")
                        break
                else:
                    print(f"Categoria com ID {id_categoria} não encontrada.")
                
            elif alterar == 4:
                mostrar_fornecedores()
                id_fornecedor = int(input("Digite o ID do fornecedor que deseja alterar: "))
                fornecedores = FornecedorDAO.listar()
                for fornecedor in fornecedores:
                    if fornecedor.id_fornecedor == int(id_fornecedor):
                        dado = int(input("Qual dado deseja alterar? \n1 - Nome\n2 - CNPJ\nEscolha uma opção: "))
                        if dado == 1:
                            novo_nome = input("Digite o novo nome: ")
                            FornecedorDAO.alterar_nome(fornecedor.id_fornecedor, novo_nome)
                            print(f"Nome do fornecedor {fornecedor.nome} alterado para {novo_nome}.")
                        elif dado == 2:
                            novo_cnpj = input("Digite o novo CNPJ: ")
                            FornecedorDAO.alterar_cnpj(fornecedor.id_fornecedor, novo_cnpj)
                            print(f"CNPJ do fornecedor {fornecedor.nome} alterado para {novo_cnpj}.")
                        else:
                            print("Opção inválida. Tente novamente.")
                        break
                else:
                    print(f"Fornecedor com ID {id_fornecedor} não encontrado.")
                
            elif alterar == 5:
                mostrar_produtos()
                id_produto = int(input("Digite o ID do produto que deseja alterar: "))
                produtos = ProdutoDAO.listar()
                for produto in produtos:
                    if produto.id_produto == int(id_produto):
                        dado = int(input("Qual dado deseja alterar? \n1 - Nome\n2 - Preço\n3 - Categoria\n4 - Fornecedor\nEscolha uma opção: "))
                        if dado == 1:
                            novo_nome = input("Digite o novo nome: ")
                            ProdutoDAO.alterar_nome(produto.id_produto, novo_nome)
                            print(f"Nome do produto {produto.nome} alterado para {novo_nome}.")
                        elif dado == 2:
                            novo_preco = float(input("Digite o novo preço: "))
                            ProdutoDAO.alterar_preco(produto.id_produto, novo_preco)
                            print(f"Preço do produto {produto.nome} alterado para {novo_preco}.")
                        elif dado == 3:
                            mostrar_categorias()
                            categorias = CategoriaDAO.listar()
                            novo_id_categoria = int(input("Digite o novo ID da categoria: "))
                            for  categoria in categorias:
                                if  categoria.id_categoria == int(novo_id_categoria):
                                    ProdutoDAO.alterar_categoria(produto.id_produto, novo_id_categoria)
                                    print(f"Categoria do produto {produto.nome} alterada para {novo_id_categoria}.")
                                    break
                            else:
                                print(f"Categoria com ID {novo_id_categoria} não encontrada.")
                        elif dado == 4:
                            mostrar_fornecedores()
                            novo_id_fornecedor = int(input("Digite o novo ID do fornecedor: "))
                            for fornecedor in FornecedorDAO.listar():
                                if fornecedor.id_fornecedor == int(novo_id_fornecedor):
                                    ProdutoDAO.alterar_fornecedor(produto.id_produto, novo_id_fornecedor)
                                    print(f"Fornecedor do produto {produto.nome} alterado para {novo_id_fornecedor}.")
                                    break
                            else:
                                print(f"Fornecedor com ID {novo_id_fornecedor} não encontrado.")
                        else:
                            print("Opção inválida. Tente novamente.")
                        break
                else:
                    print(f"Produto com ID {id_produto} não encontrado.")
                
        elif alterar == 9:
            break
        else:
            print("Opção inválida. Tente novamente.")