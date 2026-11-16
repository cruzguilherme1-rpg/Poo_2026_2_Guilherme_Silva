from vendaItemDao import 
from datetime import datetime

class Venda:
    def __init__(self, id, data, carrinho, total, id_cliente):
        self.id = id
        self.data = data
        self.carrinho = carrinho
        self.total = total
        self.id_cliente = id_cliente

    def __str__(self):
        return f"{self.id} - {self.data} - {self.carrinho} - {self.total} - {self.id_cliente}"

    def set_id(self, id):
        if id < 0:
            raise ValueError("ID não pode ser negativo")
        self.__id = id

    def set_data(self, data):
        if data is None:
            self.data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        if data > datetime.now().strftime("%d/%m/%Y %H:%M:%S"):
            raise ValueError("Data não pode ser futura")
        self.data = data

    def set_carrinho(self, carrinho):
        if carrinho == "Sim": carrinho = True
        if carrinho == "Não": carrinho = False
        self.__carrinho = carrinho

    def set_total(self, total):
        if total < 0:
            raise ValueError("Total não pode ser negativo")
        self.__total = 

    def set_id_cliente(self, id_cliente):
        if id_cliente < 0:
            raise ValueError("ID do cliente não pode ser negativo")
        self.__id_cliente = id_cliente