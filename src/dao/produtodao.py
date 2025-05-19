from src.model.produto import *

class CategoriaDAO:
    @classmethod
    def inserir(cls, categoria: Categoria):
        with open('categoria.txt', 'a') as file:
            file.write(f'{categoria.id_categoria};{categoria.nome}\n')
            
    @classmethod
    def listar(cls):
        categorias = []
        with open('categoria.txt', 'r') as file:
            for line in file:
                id_categoria, nome = line.strip().split(';')
                categoria = Categoria(int(id_categoria), nome)
                categorias.append(categoria)
        return categorias

class FornecedorDAO:
    @classmethod
    def inserir(cls, fornecedor: Fornecedor):
        with open('fornecedor.txt', 'a') as file:
            file.write(f'{fornecedor.id_fornecedor};{fornecedor.nome};{fornecedor.cnpj}\n')
            
    @classmethod
    def listar(cls):
        fornecedores = []
        with open('fornecedor.txt', 'r') as file:
            for line in file:
                id_fornecedor, nome, cnpj = line.strip().split(';')
                fornecedor = Fornecedor(int(id_fornecedor), nome, cnpj)
                fornecedores.append(fornecedor)
        return fornecedores

class ProdutoDAO:
    @classmethod
    def inserir(cls, produto: Produto):
        with open('produto.txt', 'a') as file:
            file.write(f'{produto.id_produto};{produto.nome};{produto.preco};{produto.categoria.id_categoria};{produto.fornecedor.id_fornecedor}\n')
            
    @classmethod
    def listar(cls):
        produtos = []
        with open('produto.txt', 'r') as file:
            for line in file:
                id_produto, nome, preco, id_categoria, id_fornecedor = line.strip().split(';')
                categoria = Categoria(int(id_categoria), "")
                fornecedor = Fornecedor(int(id_fornecedor), "", "")
                produto = Produto(int(id_produto), nome, float(preco), categoria, fornecedor)
                produtos.append(produto)
        return produtos