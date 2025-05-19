from src.dao.pessoadao import *
from src.dao.produtodao import *
#Função para gerar ID baseado no último ID cadastrado, vai buscar o último ID cadastrado e somar 1
def gerar_id(cliente=False, funcionario=False, produto=False, categoria=False, fornecedor=False):
    if cliente:
        ultimo_id = len(ClienteDAO.listar())
    elif funcionario:
        ultimo_id = len(FuncionarioDAO.listar())
    elif produto:
        ultimo_id = len(ProdutoDAO.listar())
    elif categoria:
        ultimo_id = len(CategoriaDAO.listar())
    elif fornecedor:
        ultimo_id = len(FornecedorDAO.listar())
    else:
        raise ValueError("Nenhum tipo de ID especificado. Use 'cliente', 'funcionario', 'produto', 'categoria' ou 'fornecedor'.")
    return ultimo_id + 1 if ultimo_id is not None else 1