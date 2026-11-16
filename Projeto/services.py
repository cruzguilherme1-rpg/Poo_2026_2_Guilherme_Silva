from datetime import datetime

from models.Cliente import Cliente
from models.ClienteDAO import ClienteDAO

from models.venda import Vendas
from models.vendaDAO import VendaDAO

from models.VendaItem import VendaItem
from models.VendaItemDAO import VendaItemDAO

from models.produto import Produto
from models.ProdutoDAO import ProdutoDAO

from models.categoria import Categoria


#coisas do cliente
class Service:
    @staticmethod
    def inserir_cliente(nome, email, fone):
        c = Cliente(0, nome, email, fone)
        ClienteDAO().inserir(c)

    @staticmethod
    def listar_clientes():
        return ClienteDAO().listar()

    @staticmethod
    def atualizar_cliente(id, nome, email, fone):
        c = Cliente(id, nome, email, fone)
        ClienteDAO().atualizar(c)

    @staticmethod
    def excluir_cliente(id):
        ClienteDAO().excluir(id)

#coisas das vendas

    @staticmethod
    def inserir_venda(data, carrinho, total, id_cliente):
        v = Vendas(0, data, carrinho, total, id_cliente)
        VendaDAO().inserir(v)
    
    @staticmethod
    def listar_vendas():
        return VendaDAO().listar()

    @staticmethod
    def listar_vendas_por_id(id):
        return VendaDAO().listar_id(id)

    @staticmethod
    def atualizar_venda(id, data, carrinho, total, id_cliente):
        v = Vendas(id, data, carrinho, total, id_cliente)
        VendaDAO().atualizar(v)

    @staticmethod
    def excluir_venda(id):
        VendaDAO().excluir(id)

    @staticmethod
    def inserir_produto(nome, preco, quantidade):
        p = Produto(0, nome, preco, quantidade)
        ProdutoDAO().inserir(p)

    @staticmethod
    def listar_produtos():
        return ProdutoDAO().listar()

    @staticmethod
    def atualizar_produto(id, nome, preco, quantidade):
        p = Produto(id, nome, preco, quantidade)
        ProdutoDAO().atualizar(p)

    @staticmethod
    def excluir_produto(id):
        ProdutoDAO().excluir(id)
    