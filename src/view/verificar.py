from ..controller.escolherproduto import mostrar_produtos
from ..controller.escolhercliente import mostrar_clientes
from ..controller.escolherfornecedor import mostrar_fornecedores
from ..controller.escolhercategoria import mostrar_categorias
from ..controller.escolherfuncionario import mostrar_funcionarios

def view_verificar():
    while True:
        listar = int(input("O que deseja Verificar \n1 - cliente\n2 - funcionário\n3 - categorias \n4 - fornecedores \n5 - produtos \n9 - voltar \nEscolha uma opção: "))
        if listar in [1 , 2, 3, 4, 5]:
            if listar == 1:
                mostrar_clientes()
            elif listar == 2:
                mostrar_funcionarios()
            elif listar == 3:
                mostrar_categorias()
            elif listar == 4:
                mostrar_fornecedores()
            elif listar == 5:
                mostrar_produtos()
        elif listar == 9:
            break
        else:
            print("Opção inválida. Tente novamente.\n" + ("-" * 30))