from ..controller.escolhercliente import mostrar_clientes
from ..controller.escolherfuncionario import mostrar_funcionarios
from ..controller.escolhercategoria import mostrar_categorias
from ..controller.escolherfornecedor import mostrar_fornecedores
from ..controller.escolherproduto import mostrar_produtos
from ..dao.pessoadao import *
from ..dao.produtodao import *

#TODO: Possivel erro ao excluir alguma categoria ou fornecedor e ele existir em algum produto e no local ficar meencionado None

def view_excluir():
    while True:
        excluir = int(input("O que deseja excluir \n1 - cliente\n2 - funcionário\n3 - categorias \n4 - fornecedores \n5 - produtos \n9 - voltar \nEscolha uma opção: "))
        
        if excluir in [1, 2, 3, 4, 5]:
            if excluir == 1:
                mostrar_clientes()
                id_cliente = int(input("Digite o ID do cliente que deseja excluir: "))
                for cliente in ClienteDAO.listar():
                    if cliente.id_cliente == int(id_cliente):
                        ClienteDAO.excluir(id_cliente)
                        break
                else:
                    print(f"Cliente com ID {id_cliente} não encontrado.")
                
                
            elif excluir == 2:
                mostrar_funcionarios()
                id_funcionario = int(input("Digite o ID do funcionário que deseja excluir: "))
                for funcionario in FuncionarioDAO.listar():
                    if funcionario.id_func == int(id_funcionario):
                        FuncionarioDAO.excluir(id_funcionario)
                        break
                else:
                    print(f"Funcionário com ID {id_funcionario} não encontrado.")
                
            elif excluir == 3:
                mostrar_categorias()
                id_categoria = int(input("Digite o ID da categoria que deseja excluir: "))
                for categoria in CategoriaDAO.listar():
                    if categoria.id_categoria == int(id_categoria):
                        CategoriaDAO.excluir(id_categoria)
                        break
                else:
                    print(f"Categoria com ID {id_categoria} não encontrada.")
                
            elif excluir == 4:
                mostrar_fornecedores()
                id_fornecedor = int(input("Digite o ID do fornecedor que deseja excluir: "))
                for fornecedor in FornecedorDAO.listar():
                    if fornecedor.id_fornecedor == int(id_fornecedor):
                        FornecedorDAO.excluir(id_fornecedor)
                        break
                else:
                    print(f"Fornecedor com ID {id_fornecedor} não encontrado.")
                
            elif excluir == 5:
                mostrar_produtos()
                id_produto = int(input("Digite o ID do produto que deseja excluir: "))
                for produto in ProdutoDAO.listar():
                    if produto.id_produto == int(id_produto):
                        ProdutoDAO.excluir(id_produto)
                        break
                else:
                    print(f"Produto com ID {id_produto} não encontrado.")
                
        elif excluir == 9:
            break
        else:
            print("Opção inválida. Tente novamente.\n" + ("-" * 30))
    