from src.model.pessoa import *

class ClienteDAO:
    @classmethod
    def inserir(cls, cliente: Cliente):
        with open('cliente.txt', 'a') as file:
            file.write(f'{cliente.nome};{cliente.idade};{cliente.id_cliente}\n')
    
    @classmethod
    def listar(cls):
        clientes = []
        with open('cliente.txt', 'r') as file:
            for line in file:
                nome, idade, id_cliente = line.strip().split(';')
                cliente = Cliente(nome, int(idade), int(id_cliente))
                clientes.append(cliente)
        return clientes
    
class FuncionarioDAO:
    @classmethod
    def inserir(cls, funcionario: Funcionario):
        with open('funcionario.txt', 'a') as file:
            file.write(f'{funcionario.nome};{funcionario.idade};{funcionario.cargo};{funcionario.id_func};{funcionario.salario}\n')
    
    @classmethod
    def listar(cls):
        funcionarios = []
        with open('funcionario.txt', 'r') as file:
            for line in file:
                nome, idade, cargo, id_func, salario = line.strip().split(';')
                funcionario = Funcionario(nome, int(idade), cargo, int(id_func), float(salario))
                funcionarios.append(funcionario)
        return funcionarios