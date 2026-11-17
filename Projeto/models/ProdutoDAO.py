import json 
from .produto import Produto

class ProdutoDAO:
    def __init__(self):
        self.__arquivo = "PRODUTO.json"
        self.__objetos = []

    def salvar(self):
        with open(self.__arquivo, "w") as f:
            json.dump([p.to_json() for p in self.__objetos], f)

    def carregar(self):
        try:
            with open(self.__arquivo, "r") as f:
                data = json.load(f)
                self.__objetos = [Produto.from_json(p) for p in data]
        except FileNotFoundError:
            pass

    def inserir(self, produto):
        self.__objetos.append(produto)
        self.salvar()

    def listar(self):
        return self.__objetos

    def atualizar(self, produto):
        for i, p in enumerate(self.__objetos):
            if p.get_id() == produto.get_id():
                self.__objetos[i] = produto
                break
        self.salvar()

    def excluir(self, produto):
        self.__objetos.remove(produto)
        self.salvar()