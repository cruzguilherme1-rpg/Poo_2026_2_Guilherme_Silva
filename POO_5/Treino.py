import datetime

#OBS: decidi adicionar a informação de nome para melhor comunicação em relação ao treino

class Treino:
    def __init__(self,nome, id, data, distancia, tempo_total):
        self.set_nome(nome) 
        self.set_id(id)
        self.set_data(data)
        self.set_distancia(distancia)
        self.set_tempo_total(tempo_total)


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

    #tempo_total
    def set_tempo_total(self, tempo_total):
        self.__tempo_total = tempo_total
    def get_tempo_total(self): return self.__tempo_total

class UI:
    treinos = []
    @staticmethod
    def main():
        op = 0
        while op != 7:
            op = UI.menu()
            if op == 1: UI.inserir_treino()
            if op == 2: UI.listar_treino()
            if op == 3: UI.listar_id()
            if op == 4: UI.atualizar_treino()   
            if op == 5: UI.excluir_treino()
            if op == 6: UI.treino_rapido()

    @staticmethod
    def menu():
        print("1 - Inserir treino")
        print("2 - Listar treino")
        print("3 - Listar por ID")  
        print("4 - Atualizar treino")  
        print("5 - Excluir treino")
        print("6 - Treino mais rápido")
        print("7 - Sair")
        return int(input("Digite a opção: "))

    @classmethod
    def inserir_treino(cls):
        id = int(input("Digite o id: "))
        data = datetime.datetime(*map(int, [input("Digite o ano: "), input("Digite o mês: "), input("Digite o dia: "), input("Digite a hora: "), input("Digite os minutos: "), input("Digite os segundos: ")]))
        distancia = float(input("Digite a distancia: "))
        nome = input("Digite o nome do treino: ")
        tempo_horas = datetime.timedelta(hours=int(input("Digite o tempo do treino (horas): ")))
        tempo_minutos = datetime.timedelta(minutes=int(input("Digite o tempo do treino (minutos): ")))
        tempo_segundos = datetime.timedelta(seconds=int(input("Digite o tempo do treino (segundos): ")))
        tempo_total = tempo_horas + tempo_minutos + tempo_segundos
        treino = Treino(nome, id, data, distancia, tempo_total)
        cls.treinos.append(treino)
        print(f"Treino {treino.get_id()} inserido com sucesso!")

    @classmethod
    def listar_treino(cls):
        if not cls.treinos:
            print("Nenhum treino cadastrado.")
            return
        print("Aqui estão todos os treinos cadastrados: ")
        for treino in cls.treinos:
            print(f"Nome: {treino.get_nome()}, ID: {treino.get_id()}, Data: {treino.get_data()}, Distância: {treino.get_distancia()}, Tempo_total: {treino.get_tempo_total()}")

    @classmethod
    def listar_id(cls):
        if not cls.treinos:
            print("Nenhum treino cadastrado.")
            return
        id = int(input("Digite o ID do treino: "))
        print("aqui estão os treinos cadastrados com o ID informado: ")
        for treino in cls.treinos:
            if treino.get_id() == id:
                    print(f"Nome: {treino.get_nome()}, ID: {treino.get_id()}, Data: {treino.get_data()}, Distância: {treino.get_distancia()}, Tempo_total: {treino.get_tempo_total()}")

    @classmethod
    def atualizar_treino(cls):
        if not cls.treinos:
            print("Nenhum treino cadastrado.")
            return
        id = int(input("Digite o ID do treino que deseja atualizar: "))
        for treino in cls.treinos:
            if treino.get_id() == id:
                data = datetime.datetime(*map(int, [input("Digite o ano: "), input("Digite o mês: "), input("Digite o dia: "), input("Digite a hora: "), input("Digite os minutos: "), input("Digite os segundos: ")]))
                distancia = float(input("Digite a distancia: "))
                nome = input("Digite o nome do treino: ")
                treino.set_nome(nome)
                treino.set_data(data)
                treino.set_distancia(distancia)
                tempo_horas = datetime.timedelta(hours=int(input("Digite o tempo do treino (horas): ")))
                tempo_minutos = datetime.timedelta(minutes=int(input("Digite o tempo do treino (minutos): ")))
                tempo_segundos = datetime.timedelta(seconds=int(input("Digite o tempo do treino (segundos): ")))
                tempo_total = tempo_horas + tempo_minutos + tempo_segundos  
                treino.set_tempo_total(tempo_total)
                print(f"Treino {treino.get_id()} atualizado com sucesso!")
                return
        print(f"Treino com ID {id} não encontrado.")

    @classmethod
    def excluir_treino(cls):
        if not cls.treinos:
            print("Nenhum treino cadastrado.")
            return
        id = int(input("Digite o ID do treino que deseja excluir: "))
        for treino in cls.treinos:
            if treino.get_id() == id:
                cls.treinos.remove(treino)
                print(f"Treino {treino.get_id()} excluído com sucesso!")
                return
        print(f"Treino com ID {id} não encontrado.")

    @classmethod
    def treino_rapido(cls):
        if not cls.treinos:
            print("Nenhum treino cadastrado.")
            return
        treino_mais_rapido = min(cls.treinos, key=lambda t: t.get_tempo_total())
        print(f"Treino mais rápido: Nome: {treino_mais_rapido.get_nome()}, ID: {treino_mais_rapido.get_id()}, Data: {treino_mais_rapido.get_data()}, Distância: {treino_mais_rapido.get_distancia()}, Tempo_total: {treino_mais_rapido.get_tempo_total()}")

UI.main()