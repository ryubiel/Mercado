class Categoria:
    def __init__(self, id_categoria, nome):
        self.id_categoria = id_categoria
        self.nome = nome
        
class Fornecedor:
    def __init__(self, id_fornecedor, nome, cnpj):
        self.id_fornecedor = id_fornecedor
        self.nome = nome
        self.cnpj = cnpj
        
class Produto:
    def __init__(self, id_produto, nome, preco, categoria: Categoria, fornecedor: Fornecedor):
        self.id_produto = id_produto 
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.fornecedor = fornecedor
        