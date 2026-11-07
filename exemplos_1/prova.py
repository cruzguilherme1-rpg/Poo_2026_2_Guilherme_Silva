class Financeamento:
    def __init__(self, nome, valor, entrada, parcelas):
        self.set_nome(nome)
        self.set_valor(valor)
        self.set_entrada(entrada)
        self.set_parcelas(parcelas)

    def set_nome(self, nome):
        if nome == "": raise ValueError("nome deve ser informado")
        else: self.__nome = nome
    def get_nome(self):
        return self.__nome

    def set_valor(self, valor):
        if valor < 0: raise ValueError("valor deve ser informado")
        else: self.__valor = valor
    def get_valor(self):
        return self.__valor

    def set_entrada(self, entrada):
        if entrada < 0 : raise ValueError("entrada deve ser informado")
        else: self.__entrada = entrada
    def get_entrada(self):
        return self.__entrada

    def set_parcelas(self, parcelas):
            if parcelas < 1 or parcelas > 36: raise ValueError("parcelas deve ser entre 1 e 36")
            else: self.__parcelas = parcelas
    def get_parcelas(self):
        return self.__parcelas

    def valor_a_vista(self):
        return self.__valor * 0.95
    def valor_da_parcela(self):
        return (self.__valor - self.__entrada) / self.__parcelas

    def __str__(self):
        return f"nome do carro: {self.__nome}, valor do carro: {self.__valor}, entrada: {self.__entrada}, total de parcelas: {self.__parcelas}"

class UI:
    @staticmethod 
    def main():
        op = 0
        while op != 2:
            op = UI.menu()
            if op == 1: UI.calculo()


    @staticmethod 
    def menu():
        print("1 - Finaciamento, 2 - fim")
        return (int(input("escolha uma opcao: ")))

    @staticmethod 
    def calculo():
        nome = input("nome do carro: ")
        valor = float(input("valor do carro: "))
        entrada = float(input("valor da entrada: "))
        parcelas = int(input("total de parcelas: "))
        x = Financeamento(nome, valor, entrada, parcelas)

        print("valor a vista: ",x.valor_a_vista)
        print("valor das parcelas: ",x.valor_da_parcela)

UI.main()
