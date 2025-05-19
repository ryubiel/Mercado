from ..model.pessoa import *
from ..model.produto import *
from ..dao.pessoadao import *
from ..dao.produtodao import *
from ..controller.id import gerar_id
from ..controller.escolhercategoria import escolher_categoria
from ..controller.escolherfornecedor import escolher_fornecedor

from time import sleep
from .cadastrar import view_cadastrar
from .verificar import view_verificar

def view():
    while True:
        escolha = int(input("Sistema do mercado\n1 - Cadastrar \n2 - Alterar \n3 - Remover \n4 - Verificar \n5 - Caixa\n6 - Relatório \n9 - Sair\nEscolha uma opção: "))
        if escolha == 9:
            break
        elif escolha == 1:
            view_cadastrar()
        elif escolha == 2:
            print("Opção de alterar não implementada.")
        elif escolha == 3:
            print("Opção de remover não implementada.")
        elif escolha == 4:
            view_verificar()
        elif escolha == 5:
            print("Opção de caixa não implementada.")
        elif escolha == 6:
            print("Opção de relatório não implementada.")
        else:
            print("Opção inválida. Tente novamente.")
            sleep(0.5)
        