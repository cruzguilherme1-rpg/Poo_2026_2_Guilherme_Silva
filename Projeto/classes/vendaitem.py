class VendaItem:
    def __init__(self, id, qtd, preco, id_venda, id_produto):
        self.set_id(id)
        self.set_qtd(qtd)
        self.set_preco(preco)
        self.set_id_venda(id_venda)
        self.set_id_produto(id_produto)

    def set_id(self, id):