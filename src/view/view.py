from .cadastrar import view_cadastrar
from .verificar import view_verificar
from .alterar import view_alterar
from .excluir import view_excluir

def view():
    while True:
        escolha = int(input("Sistema do mercado\n1 - Cadastrar \n2 - Alterar \n3 - Remover \n4 - Verificar \n5 - Caixa\n6 - Relatório \n9 - Sair\nEscolha uma opção: "))
        if escolha == 9:
            break
        elif escolha == 1:
            view_cadastrar()
        elif escolha == 2:
            view_alterar()
        elif escolha == 3:
            view_excluir()
        elif escolha == 4:
            view_verificar()
        elif escolha == 5:
            print("Opção de caixa não implementada.")
        elif escolha == 6:
            print("Opção de relatório não implementada.")
        else:
            print("Opção inválida. Tente novamente.")
        