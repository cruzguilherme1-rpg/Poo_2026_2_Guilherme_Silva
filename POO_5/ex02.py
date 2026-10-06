import enum
from datetime import datetime,timedelta

class SituacaoEstagio(enum.Enum):
    cadastro = 1
    iniciado = 2
    cancelado = 3
    finalizado = 4

class Estagio:
    def __init__(self, est, emp):
        self.set_estagiario(est)
        self.set_empresa(emp)
        self.data_inicio = None
        self.data_cancelamento = None
        self.data_fim = None
        self.data_situacao = SituacaoEstagio.cadastro

    def set_estagiario(self, est):
        if est == "": raise ValueError("Estagiário deve ser informado")
        self.__estagiario = est

    def set_empresa(self, emp):
        if emp == "": raise ValueError("Empresa deve ser informada")
        self.__empresa = emp

    def get_estagio(self): return self.__estagiario
    def get_empresa(self): return self.__empresa

    def iniciar(self, data):
        if self.__situacao != SituacaoEstagio.iniciado: raise ValueError("Só é possivel iniciar um estagio cadastrado ")
        self.__data_inicio = data
        self.__situacao = SituacaoEstagio.iniciado

    def cancelar(self, data):
        if self.__situacao != SituacaoEstagio.iniciado: raise ValueError("Só é possivel cancelar um estagio não finalizado")
        self.__cancelamento = data
        self.__situacao = SituacaoEstagio.cancelado

    def finalizar(self, data):
        if self.__situacao != SituacaoEstagio.iniciado: raise ValueError("Só é possivel finalizar um estagio iniciado")
        self.__data_fim = data
        self.__situacao = SituacaoEstagio.finalizado

    def tempo_estagio(self):
        if self.__situacao == SituacaoEstagio.cadastro: return timedelta(0)
        if self.__situacao == SituacaoEstagio.iniciado: return datetime.now() - self.__data_inicio
        if self.__situacao == SituacaoEstagio.cancelado: return self.__data_cancelamento - self.__data_inicio

    def __str__(self):
        s = f"{self.__estagiario} - {self.__empresa}"
        if self.__situacao == SituacaoEstagio.cadastro: return s + " - aguardando inicio"
        if self.__situacao == SituacaoEstagio.iniciado: return s + f"iniciado em {self.__data_inicio.strftime('%d/%m/%Y')}"
        if self.__situacao == SituacaoEstagio.cancelado: return s + f"cancelado em {self.__data_inicio.strftime('%d/%m/%Y')}"

"""
a = Estagio("Pedro", "IFRN")
b = Estagio("Lucas", "UFRN")
c = Estagio("Guilherme", "Nasa")
d = Estagio("Daniele", "INSS")

print(a)
print(b)
print(c)
print(d)

"""

class UI:
    estagios = []
    @staticmethod
    def main():
        op = 0 
        while op != 9:
            op = UI.menu()
            if op == 1: UI.inserir()
            if op == 2: UI.listar_empresa()

    @staticmethod
    def menu():
        print("1 - Inserir,  2 - listar ordenado por empresa, 9 - fim")
        return int(input("digite sua opcao: "))

    @classmethod
    def inserir(cls):
        estagiario = input("informe o nome do estagiario: ")
        empresa = input("informe o nome da empresa: ")
        x = Estagio(estagiario, empresa)
        cls.estagios.append(x)

    @classmethod
    def listar_empresa(cls):
        cls.estagios.sort(key = lambda x : x.get_empresa() + x.get_estagio() )
        for x in cls.estagios:
            print(x)

UI.main()