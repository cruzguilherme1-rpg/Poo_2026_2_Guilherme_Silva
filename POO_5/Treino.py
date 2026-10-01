import datetime

#OBS: decidi adicionar a informação de nome para melhor comunicação em relação ao treino

class Treino:
    def __init__(self,nome, id, data, distancia, tempo):
        self.set_nome(nome) 
        self.set_id(id)
        self.set_data(data)
        self.set_distancia(distancia)
        self.set_tempo(tempo)
    
    #nome
    def set_nome(self, nome):
        if nome == "": raise ValueError("nome deve ser informado")
        self.__nome = nome
    def get_nome(self): return self.__nome

    #id
    def set_id(self, id):
       if id <= 0 or id is None: raise ValueError("id deve ser informado")
       else: self.__id = id
    def get_id(self): return self.__id

    #data
    def set_data(self, data):
        if data == "": raise ValueError("data deve ser informada")
        self.__data = data
    def get_data(self): return self.__data

    #distancia
    def set_distancia(self, distancia):
        if distancia < 0 or distancia is None: raise ValueError("distancia deve ser informada")
        else: self.__distancia = distancia
    def get_distancia(self): return self.__distancia

    #tempo
    def set_tempo(self, tempo):
        if tempo <= 0 or tempo is None: raise ValueError("tempo deve ser informado")
        else: self.__tempo = tempo
    def get_tempo(self): return self.__tempo


class UI:
    treinos = []
    @staticmethod
    def main():
        op = 0
        while op != 5:
            op = UI.menu()
            if op == 1: UI.inserir_treino()
            if op == 2: UI.listar_treino()
            if op == 3: UI.listar_id()

    @staticmethod
    def menu():
        print("1 - Inserir treino")
        print("2 - Listar treino")
        print("3 - Listar por ID")  
        print("5 - Sair")
        return int(input("Digite a opção: "))

    @classmethod
    def inserir_treino(cls):
        id = int(input("Digite o id: "))
        data = datetime.datetime(*map(int, [input("Digite o ano: "), input("Digite o mês: "), input("Digite o dia: "), input("Digite a hora: "), input("Digite os minutos: "), input("Digite os segundos: ")]))
        distancia = float(input("Digite a distancia: "))
        tempo = datetime.timedelta(*map(int, [input("Digite o ano: "), input("Digite o mês: "), input("Digite o dia: "), input("Digite a hora: "), input("Digite os minutos: "), input("Digite os segundos: ")]))
        nome = input("Digite o nome do treino: ")
        treino = Treino(nome, id, data, distancia, tempo)
        cls.treinos.append(treino)
        print(f"Treino {treino.get_id()} inserido com sucesso!")

    @classmethod
    def listar_treino(cls):
        print("Aqui estão todos os treinos cadastrados: ")
        for treino in cls.treinos:
            print(f"Nome: {treino.get_nome()}, ID: {treino.get_id()}, Data: {treino.get_data()}, Distância: {treino.get_distancia()}, Tempo: {treino.get_tempo()}")

    @classmethod
    def listar_id(cls):
        id = int(input("Digite o ID do treino: "))
        print("aqui estão os treinos cadastrados com o ID informado: ")
        for treino in cls.treinos:
            if treino.get_id() == id:
                    print(f"Nome: {treino.get_nome()}, ID: {treino.get_id()}, Data: {treino.get_data()}, Distância: {treino.get_distancia()}, Tempo: {treino.get_tempo()}")

UI.main()
