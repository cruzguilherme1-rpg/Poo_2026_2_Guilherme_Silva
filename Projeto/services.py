from models.Cliente import Cliente
from models.ClienteDAO import ClienteDAO

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