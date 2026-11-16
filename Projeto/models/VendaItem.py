class VendaItem:
    def __init__(self, id, quantidade, preco, id_venda, id_produto):
        self.set_id(id)
        self.set_quantidade(quantidade)
        self.set_preco(preco)
        self.set_id_venda(id_venda)
        self.set_id_produto(id_produto)

    def __str__(self):
        return f"{self.id} - {self.quantidade} - {self.preco} - {self.id_venda} - {self.id_produto}"
    
    def set_id(self, id):  
        if id < 0:
            raise ValueError("ID não pode ser negativo")
        self.__id = id

    def set_quantidade(self, quantidade):
        if quantidade < 0:
            raise ValueError("Quantidade não pode ser negativa")
        self.__quantidade = quantidade

    def set_preco(self, preco):
        if preco < 0.0:
            raise ValueError("Preço não pode ser negativo")
        self.__preco = preco

    def set_id_venda(self, id_venda):
        if id_venda <= 0:
            raise ValueError("ID da venda não pode ser menor que 0")
        self.__id_venda = id_venda

    def set_id_produto(self, id_produto):
        if id_produto <= 0:
            raise ValueError("ID do produto não pode ser menor que 0")
        self.__id_produto = id_produto

    def get_id(self): return self.__id
    def get_quantidade(self): return self.__quantidade  
    def get_preco(self): return self.__preco
    def get_id_venda(self): return self.__id_venda
    def get_id_produto(self): return self.__id_produto

    def to_json(self):
        VENDAITEM = {}
        VENDAITEM["id"] = self.get_id()
        VENDAITEM["quantidade"] = self.get_quantidade()
        VENDAITEM["preco"] = self.get_preco()
        VENDAITEM["id_venda"] = self.get_id_venda()
        VENDAITEM["id_produto"] = self.get_id_produto()
        return VENDAITEM

    @staticmethod
    def from_json(VENDAITEM):
        return VendaItem(VENDAITEM["id"], VENDAITEM["quantidade"], VENDAITEM["preco"], VENDAITEM["id_venda"], VENDAITEM["id_produto"])