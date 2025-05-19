class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
        
class Funcionario(Pessoa):
    def __init__(self, nome: str, idade: int, cargo: str, id_func: int, salario: float):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.id_func = id_func
        self.salario = salario
        
class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int, id_cliente: int):
        super().__init__(nome, idade)
        self.id_cliente = id_cliente