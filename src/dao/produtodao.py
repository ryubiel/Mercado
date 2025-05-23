from src.model.produto import *

class CategoriaDAO:
    @classmethod
    def inserir(cls, categoria: Categoria):
        with open('dados/categoria.txt', 'a') as file:
            file.write(f'{categoria.id_categoria};{categoria.nome}\n')
            print(f'Categoria {categoria.nome} cadastrada com sucesso!')
            
    @classmethod
    def listar(cls):
        categorias = []
        with open('dados/categoria.txt', 'r') as file:
            for line in file:
                id_categoria, nome = line.strip().split(';')
                categoria = Categoria(int(id_categoria), nome)
                categorias.append(categoria)
        return categorias
    
    @classmethod
    def excluir(cls, id_categoria):
        categorias = cls.listar()
        categorias_excluir = [categoria for categoria in categorias if categoria.id_categoria != id_categoria]
        with open('dados/categoria.txt', 'w') as file:
            for categoria in categorias_excluir:
                file.write(f'{categoria.id_categoria};{categoria.nome}\n')
            print(f'Categoria com ID {id_categoria} excluída com sucesso!')
    
    @classmethod
    def alterar_nome(cls, id_categoria, novo_nome):
        categorias = cls.listar()
        for categoria in categorias:
            if categoria.id_categoria == id_categoria:
                categoria.nome = novo_nome
                break
        with open('dados/categoria.txt', 'w') as file:
            for categoria in categorias:
                file.write(f'{categoria.id_categoria};{categoria.nome}\n')

class FornecedorDAO:
    @classmethod
    def inserir(cls, fornecedor: Fornecedor):
        with open('dados/fornecedor.txt', 'a') as file:
            file.write(f'{fornecedor.id_fornecedor};{fornecedor.nome};{fornecedor.cnpj}\n')
            print(f'Fornecedor {fornecedor.nome} cadastrado com sucesso!')
            
    @classmethod
    def listar(cls):
        fornecedores = []
        with open('dados/fornecedor.txt', 'r') as file:
            for line in file:
                id_fornecedor, nome, cnpj = line.strip().split(';')
                fornecedor = Fornecedor(int(id_fornecedor), nome, cnpj)
                fornecedores.append(fornecedor)
        return fornecedores
    
    @classmethod
    def excluir(cls, id_fornecedor):
        fornecedores = cls.listar()
        fornecedores_excluir = [fornecedor for fornecedor in fornecedores if fornecedor.id_fornecedor != id_fornecedor]
        with open('dados/fornecedor.txt', 'w') as file:
            for fornecedor in fornecedores_excluir:
                file.write(f'{fornecedor.id_fornecedor};{fornecedor.nome};{fornecedor.cnpj}\n')
            print(f'Fornecedor com ID {id_fornecedor} excluído com sucesso!')
    
    @classmethod
    def alterar_nome(cls, id_fornecedor, novo_nome):
        fornecedores = cls.listar()
        for fornecedor in fornecedores:
            if fornecedor.id_fornecedor == id_fornecedor:
                fornecedor.nome = novo_nome
                break
        with open('dados/fornecedor.txt', 'w') as file:
            for fornecedor in fornecedores:
                file.write(f'{fornecedor.id_fornecedor};{fornecedor.nome};{fornecedor.cnpj}\n')
                
    @classmethod
    def alterar_cnpj(cls, id_fornecedor, novo_cnpj):
        fornecedores = cls.listar()
        for fornecedor in fornecedores:
            if fornecedor.id_fornecedor == id_fornecedor:
                fornecedor.cnpj = novo_cnpj
                break
        with open('dados/fornecedor.txt', 'w') as file:
            for fornecedor in fornecedores:
                file.write(f'{fornecedor.id_fornecedor};{fornecedor.nome};{fornecedor.cnpj}\n')

class ProdutoDAO:
    @classmethod
    def inserir(cls, produto: Produto):
        with open('dados/produto.txt', 'a') as file:
            file.write(f'{produto.id_produto};{produto.nome};{produto.preco};{produto.categoria.id_categoria};{produto.fornecedor.id_fornecedor}\n')
            print(f'Produto {produto.nome} cadastrado com sucesso!')
            
    @classmethod
    def listar(cls):
        produtos = []
        with open('dados/produto.txt', 'r') as file:
            for line in file:
                id_produto, nome, preco, id_categoria, id_fornecedor = line.strip().split(';')
                categoria = Categoria(int(id_categoria), "")
                fornecedor = Fornecedor(int(id_fornecedor), "", "")
                produto = Produto(int(id_produto), nome, float(preco), categoria, fornecedor)
                produtos.append(produto)
        return produtos
    
    @classmethod
    def excluir(cls, id_produto):
        produtos = cls.listar()
        produtos_excluir = [produto for produto in produtos if produto.id_produto != id_produto]
        with open('dados/produto.txt', 'w') as file:
            for produto in produtos_excluir:
                file.write(f'{produto.id_produto};{produto.nome};{produto.preco};{produto.categoria.id_categoria};{produto.fornecedor.id_fornecedor}\n')
            print(f'Produto com ID {id_produto} excluído com sucesso!')
    
    @classmethod
    def alterar_nome(cls, id_produto, novo_nome):
        produtos = cls.listar()
        for produto in produtos:
            if produto.id_produto == id_produto:
                produto.nome = novo_nome
                break
        with open('dados/produto.txt', 'w') as file:
            for produto in produtos:
                file.write(f'{produto.id_produto};{produto.nome};{produto.preco};{produto.categoria.id_categoria};{produto.fornecedor.id_fornecedor}\n')
                
    @classmethod
    def alterar_preco(cls, id_produto, novo_preco):
        produtos = cls.listar()
        for produto in produtos:
            if produto.id_produto == id_produto:
                produto.preco = novo_preco
                break
        with open('dados/produto.txt', 'w') as file:
            for produto in produtos:
                file.write(f'{produto.id_produto};{produto.nome};{produto.preco};{produto.categoria.id_categoria};{produto.fornecedor.id_fornecedor}\n')
                
    @classmethod
    def alterar_categoria(cls, id_produto, nova_categoria):
        produtos = cls.listar()
        for produto in produtos:
            if produto.id_produto == id_produto:
                produto.categoria.id_categoria = nova_categoria
                break
        with open('dados/produto.txt', 'w') as file:
            for produto in produtos:
                file.write(f'{produto.id_produto};{produto.nome};{produto.preco};{produto.categoria.id_categoria};{produto.fornecedor.id_fornecedor}\n')
                
    @classmethod
    def alterar_fornecedor(cls, id_produto, novo_fornecedor):
        produtos = cls.listar()
        for produto in produtos:
            if produto.id_produto == id_produto:
                produto.fornecedor.id_fornecedor = novo_fornecedor
                break
        with open('dados/produto.txt', 'w') as file:
            for produto in produtos:
                file.write(f'{produto.id_produto};{produto.nome};{produto.preco};{produto.categoria.id_categoria};{produto.fornecedor.id_fornecedor}\n')
                
    