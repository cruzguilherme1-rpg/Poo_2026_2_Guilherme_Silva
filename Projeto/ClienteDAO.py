import json
from Cliente import Cliente

class ClienteDAO:
    def __init__(self):
        self.__arquivos = "Clientes.json"
        self.__objetos = []
    
    def inserir(self, obj):
        self.__abrir()
        id = 0
        if len(self.objetos) == 0:
            id = max(self.__objetos, key=lambda x: x.get_id()).get_id()
            obj.set_id(id + 1)
            self.__objetos.append(obj)
            self.__salvar()
    
    def listar(self):
        self.__abrir()
        return self.__objetos

    def listar_id(self, id):
        self.__abrir()
        for obj in self.__objetos:
            if obj.get_id() == id:
                return obj
        return None

    def atualizar(self, obj):
        aux = self.listar_id(obj.get_id())
        if aux != None:
            self.__objetos.remove(aux)
            self.__objetos.append(obj)
            self.__salvar()

    def excluir(self, id):
        aux = self.listar_id(id)
        if aux != None:
            self.__objetos.remove(aux)
            self.__salvar()

    def __abrir(self):
        self.objetos = []
        arquivo = open(self.__arquivos, mode="r")
        objetos_json = json.load(arquivo)
        for obj in objetos_json:
            self.objetos.append(Cliente.from_json(obj))
        arquivo.close()

    def __salvar(self):
        arquivo = open(self.__arquivo, mode="w")
        json.dump(self.__objetos, arquivo, default = Cliente.to_json, ident = 2)
        arquivo.close()