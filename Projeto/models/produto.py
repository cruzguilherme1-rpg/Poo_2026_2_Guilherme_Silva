class Produto:
    def __init__(self, id, descricao, preco, estoque, id_categoria):
        self.set_id(id)
        self.set_descricao(descricao)
        self.set_preco(preco)
        self.set_estoque(estoque)
        self.set_id_categoria(id_categoria)

    def __str__(self):
        return f"{self.get_id()} - {self.get_descricao()} - {self.get_preco()} - {self.get_estoque()} - {self.get_id_categoria()}"

    def set_id(self, id):
        if id <= 0:
            raise ValueError("ID não pode ser negativo")
        self.__id = id
    
    def set_descricao(self, descricao):
        if descricao == "":
            raise ValueError("Descrição não pode ser vazia")
        self.__descricao = descricao

    def set_preco(self, preco):
        if preco < 0.0:
            raise ValueError("Preço não pode ser negativo")
        self.__preco = preco

    def set_estoque(self, estoque):
        if estoque == 0:
            raise ValueError("Estoque está vazio")
        if estoque < 0:
            raise ValueError("Estoque não pode ser negativo")
        self.__estoque = estoque

    def set_id_categoria(self, id_categoria):
        if id_categoria <= 0:
            raise ValueError("ID da categoria não pode ser negativo")
        self.__id_categoria = id_categoria

    def get_id(self): return self.__id
    def get_descricao(self): return self.__descricao
    def get_preco(self): return self.__preco
    def get_estoque(self): return self.__estoque
    def get_id_categoria(self): return self.__id_categoria
    
    def to_json(self):
        PRODUTO = {}
        PRODUTO["id"] = self.get_id()
        PRODUTO["descricao"] = self.get_descricao()
        PRODUTO["preco"] = self.get_preco()
        PRODUTO["estoque"] = self.get_estoque()
        PRODUTO["id_categoria"] = self.get_id_categoria()
        return PRODUTO

    @staticmethod
    def from_json(PRODUTO):
        return Produto(PRODUTO["id"], PRODUTO["descricao"], PRODUTO["preco"], PRODUTO["estoque"], PRODUTO["id_categoria"])