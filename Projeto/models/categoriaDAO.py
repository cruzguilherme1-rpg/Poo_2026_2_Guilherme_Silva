import json
from categoria import Categoria

class CategoriaDAO:
    def __init__(self):
        self.__arquivo = "CATEGORIA.json"
        self.__objetos = []

def salvar(self):
    with open(self.__arquivo, "w") as f:
        json.dump([c.to_json() for c in self.__objetos], f)

def carregar(self):
    try:
        with open(self.__arquivo, "r") as f:
            data = json.load(f)
            self.__objetos = [Categoria.from_json(c) for c in data]
    except FileNotFoundError:
        pass

def inserir(self, categoria):
    self.__objetos.append(categoria)
    self.salvar()

def listar(self):
    return self.__objetos

def atualizar(self, categoria):
    for i, c in enumerate(self.__objetos):
        if c.get_id() == categoria.get_id():
            self.__objetos[i] = categoria
            break
    self.salvar()

def excluir(self, categoria):
    self.__objetos.remove(categoria)
    self.salvar()   

