from src.model.pessoa import *

class ClienteDAO:
    @classmethod
    def inserir(cls, cliente: Cliente):
        with open('dados/cliente.txt', 'a') as file:
            file.write(f'{cliente.nome};{cliente.idade};{cliente.id_cliente}\n')
            print(f'Cliente {cliente.nome} inserido com sucesso!')
    
    @classmethod
    def listar(cls):
        clientes = []
        with open('dados/cliente.txt', 'r') as file:
            for line in file:
                nome, idade, id_cliente = line.strip().split(';')
                cliente = Cliente(nome, int(idade), int(id_cliente))
                clientes.append(cliente)
        return clientes
    
    @classmethod
    def excluir(cls, id_cliente):
        clientes = cls.listar()
        clientes_excluir = [cliente for cliente in clientes if cliente.id_cliente != id_cliente]
        with open('dados/cliente.txt', 'w') as file:
            for cliente in clientes_excluir:
                file.write(f'{cliente.nome};{cliente.idade};{cliente.id_cliente}\n')
        print(f'Cliente com ID {id_cliente} excluído com sucesso!')
    
    @classmethod
    def alterar_nome(cls, id_cliente, novo_nome):
        clientes = cls.listar()
        for cliente in clientes:
            if cliente.id_cliente == id_cliente:
                cliente.nome = novo_nome
                break
        with open('dados/cliente.txt', 'w') as file:
            for cliente in clientes:
                file.write(f'{cliente.nome};{cliente.idade};{cliente.id_cliente}\n')
    
    @classmethod
    def alterar_idade(cls, id_cliente, nova_idade):
        clientes = cls.listar()
        for cliente in clientes:
            if cliente.id_cliente == id_cliente:
                cliente.idade = nova_idade
                break
        with open('dados/cliente.txt', 'w') as file:
            for cliente in clientes:
                file.write(f'{cliente.nome};{cliente.idade};{cliente.id_cliente}\n')
                
class FuncionarioDAO:
    @classmethod
    def inserir(cls, funcionario: Funcionario):
        with open('dados/funcionario.txt', 'a') as file:
            file.write(f'{funcionario.nome};{funcionario.idade};{funcionario.cargo};{funcionario.id_func};{funcionario.salario}\n')
            print(f'Funcionario {funcionario.nome} inserido com sucesso!')
    
    @classmethod
    def listar(cls):
        funcionarios = []
        with open('dados/funcionario.txt', 'r') as file:
            for line in file:
                nome, idade, cargo, id_func, salario = line.strip().split(';')
                funcionario = Funcionario(nome, int(idade), cargo, int(id_func), float(salario))
                funcionarios.append(funcionario)
        return funcionarios
    
    @classmethod
    def excluir(cls, id_func):
        funcionarios = cls.listar()
        funcionarios_excluir = [funcionario for funcionario in funcionarios if funcionario.id_func != id_func]
        with open('dados/funcionario.txt', 'w') as file:
            for funcionario in funcionarios_excluir:
                file.write(f'{funcionario.nome};{funcionario.idade};{funcionario.cargo};{funcionario.id_func};{funcionario.salario}\n')
        print(f'Funcionario com ID {id_func} excluído com sucesso!')
    
    @classmethod
    def alterar_nome(cls, id_func, novo_nome):
        funcionarios = cls.listar()
        for funcionario in funcionarios:
            if funcionario.id_func == id_func:
                funcionario.nome = novo_nome
                break
        with open('dados/funcionario.txt', 'w') as file:
            for funcionario in funcionarios:
                file.write(f'{funcionario.nome};{funcionario.idade};{funcionario.cargo};{funcionario.id_func};{funcionario.salario}\n')
                
    @classmethod
    def alterar_idade(cls, id_func, nova_idade):
        funcionarios = cls.listar()
        for funcionario in funcionarios:
            if funcionario.id_func == id_func:
                funcionario.idade = nova_idade
                break
        with open('dados/funcionario.txt', 'w') as file:
            for funcionario in funcionarios:
                file.write(f'{funcionario.nome};{funcionario.idade};{funcionario.cargo};{funcionario.id_func};{funcionario.salario}\n')
                
    @classmethod
    def alterar_cargo(cls, id_func, novo_cargo):
        funcionarios = cls.listar()
        for funcionario in funcionarios:
            if funcionario.id_func == id_func:
                funcionario.cargo = novo_cargo
                break
        with open('dados/funcionario.txt', 'w') as file:
            for funcionario in funcionarios:
                file.write(f'{funcionario.nome};{funcionario.idade};{funcionario.cargo};{funcionario.id_func};{funcionario.salario}\n')
    
    @classmethod
    def alterar_salario(cls, id_func, novo_salario):
        funcionarios = cls.listar()
        for funcionario in funcionarios:
            if funcionario.id_func == id_func:
                funcionario.salario = novo_salario
                break
        with open('dados/funcionario.txt', 'w') as file:
            for funcionario in funcionarios:
                file.write(f'{funcionario.nome};{funcionario.idade};{funcionario.cargo};{funcionario.id_func};{funcionario.salario}\n')