from src.dao.pessoadao import FuncionarioDAO
from time import sleep

def mostrar_funcionarios():
    funcionarios = FuncionarioDAO.listar()
    print("Funcionarios disponíveis:")
    sleep(0.5)
    for funcionario in funcionarios:
        print(f"ID: {funcionario.id_func} - Nome: {funcionario.nome} - Idade: {funcionario.idade} - Cargo: {funcionario.cargo} - Salário: {funcionario.salario}")
        sleep(0.3)
    