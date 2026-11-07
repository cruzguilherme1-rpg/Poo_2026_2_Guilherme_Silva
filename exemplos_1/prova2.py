from datetime import datetime, timedelta

class Atleta:
    def __init__(self, i, n):
        self.set_id(i)
        self.set_nome(n)

    def set_id(self, i):
        if i < 0: raise ValueError("Id deve ser positivo")
        self.__id = i

    def set_nome(self, n):
        if n == "": raise ValueError("Nome deve ser informado")
        self.__nome = n

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome

    def __str__(self):
        return f"{self.__id} - {self.__nome}" 


class Treino:
    def __init__(self, id, id_atleta, distancia, data, tempo):
        self.set_id(id)
        self.set_id_atleta(id_atleta)
        self.set_distancia(distancia)
        self.set_data(data)
        self.set_tempo(tempo)

    def set_id(self, id):
        if id <= 0: raise ValueError("Id do treino deve ser maior que 0")
        self.__id = id

    def set_id_atleta(self, id_atleta):
        if id_atleta <= 0: raise ValueError("id_atleta do treino deve ser maior que 0")
        self.__id_atleta = id_atleta

    def set_distancia(self, distancia):
        if distancia <= 0: raise ValueError("distancia do treino deve ser maior que 0")
        self.__distancia = distancia

    def set_data(self, data):
        if data > datetime.now() : raise ValueError("data não está no passado ou presente")
        self.__data = data

    def set_tempo(self, tempo):
        if tempo < timedelta(0): raise ValueError("tempo deve ser positivo")
        self.__tempo = tempo

    def get_data(self): return self.__data
    def get_id(self): return self.__id
    def get_id_atleta(self): return self.__id_atleta
    def get_data(self): return self.__distancia
    def get_data(self): return self.__tempo

    def pace(self): return self.__tempo / self.__distancia

    def __str__(self):
        return f"{self.__id} - {self.__id_atleta} - {self.__data} - {self.__distancia} - {self.__tempo}"

class UI:
    __atletas = []
    __treinos = []

    @staticmethod
    def main():
        op = 0
        while op != 9:
            if op == 1: UI.inserir_atletas()
            if op == 2: UI.listar_atletas()
            if op == 3: UI.inserir_treino()
            if op == 4: UI.listar_treinos()
            if op == 5: UI.atleta_mais_rapido()

    def menu():
        print ("1-Inserir atleta  2-Listar atletas  3-inserir treino  4-listar treino  5-Mais rapido")
        return int(input("informe uma opção: "))

    @classmethod
    def inserir_atletas(cls):
        id = int(input("Informe o ID: "))
        nome = input("informe o nome: ")
        x = Atleta(id, nome)
        cls.__atletas.append(x)

    @classmethod
    def listar_atletas(cls):
        for x in cls.__atletas: print(x)

    @classmethod
    def inserir_treino(cls):
        id = int(input("Informe o ID: "))
        cls.listar_atletas()
        id_atleta = int(input("informe o Id do atleta: "))
        data_str = input("informe a data dd/mm/aaaa: ")
        data = datetime.strftime(data_str, "%d/%m/%Y")
        distancia = float(input("informe a distancia em km: "))
        tempo_str = input("informe o tempo MM:SS : ")
        min, seg = map(int, tempo_str.split())
        tempo = timedelta(minutes= min, seconds= seg)
        x = Treino(id, id_atleta, data, distancia, tempo)
        cls.__treinos.append(x)

    @classmethod
    def atleta_mais_rapido(cls):
        treino = min(cls.__treinos, key = lambda x : x.pace())
        for x in cls