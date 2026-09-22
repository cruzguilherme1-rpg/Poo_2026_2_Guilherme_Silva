class Triangulo:
    def __init__(self, b, h):  # Construtor
        #self.__b = 0
        #self.__h = 0
        self.set_base(b)
        self.set_altura(h)

    def __str__(self):
        return f"Triângulo com base {self.__b} e altura {self.__h}"    

    def set_base(self, v):
        if v >= 0: self.__b = v
        else: raise ValueError("Base deve ser positiva: ")    

    def set_altura(self, v):
        if v >= 0: self.__h = v
        else: raise ValueError("Altura deve ser positiva: ")

    def get_base(self):
        return self.__b        

    def get_altura(self):
        return self.__h        

    def calcular_area(self):
        return self.__b * self.__h / 2

class Retangulo:
    def __init__(self, b, h):  # Construtor
            #self.__b = 0
            #self.__h = 0
            self.set_base(b)
            self.set_altura(h)
    def __str__(self):
        return f"Retangulo com base {self.__b} e altura {self.__h}"    

    def set_base(self, v):
        if v >= 0: self.__b = v
        else: raise ValueError("Base deve ser positiva: ")    

    def set_altura(self, v):
        if v >= 0: self.__h = v
        else: raise ValueError("Altura deve ser positiva: ")

    def get_base(self):
        return self.__b        

    def get_altura(self):
        return self.__h        

    def calcular_area(self):
        return self.__b * self.__h

    def calcdiaonal(self):
        return ((self.__b**2)+(self.__h**2))**2

class Frete:
    def __init__(self, kg, km):
            self.set_peso(kg)
            self.set_distancia(km)
    def __str__(self):
        return f"frete com peso {self.__peso} e distancia {self.__distancia}"    

    def set_peso(self, v):
        if v >= 0: self.__peso = v
        else: raise ValueError("peso deve ser positivo: ")    

    def set_distancia(self, v):
        if v >= 0: self.__distancia = v
        else: raise ValueError("distancia deve ser positivo: ")

    def get_peso(self):
        return self.__peso        

    def get_distancia(self):
        return self.__distancia        

    def calcular_frete(self):
        return f"valor do frete: ", (self.__peso *0.01) * self.__distancia    

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
    def menu():
        print("1 - Triângulo, 2 - Retângulo, 3 - Frete de um pedido 9 - Fim")
        return int(input("Escolha uma opção: "))    
    @staticmethod
    def main():    
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.triangulo()    
            if op == 2: UI.retangulo()
            if op == 3: UI.frete()
    @staticmethod
    def triangulo():    
        b = float(input("Informe a base do triângulo: "))
        h = float(input("Informe a altura do triângulo: "))
        x = Triangulo(b, h)    
        print(x) 
        print(x.calcular_area()) 
    @staticmethod
    def retangulo():
        b = float(input("informe a base do retangulo")) 
        h = float(input("informe a altura do retangulo"))
        x = Retangulo(b,h)
        print(x)
        print(x.calcular_area())
        print(x.calcdiaonal())

    @staticmethod
    def frete():
        KG = float(input("informe o peso do pedido: ")) 
        KM = float(input("informe a distancia do pedido: "))
        x = Frete(KG,KM)
        print(x)
        print(x.calcular_frete())

    @staticmethod 
    def calculo():
        nome = input("nome do carro: ")
        valor = float(input("valor do carro: "))
        entrada = float(input("valor da entrada: "))
        parcelas = int(input("total de parcelas: "))
        x = Financeamento(nome, valor, entrada, parcelas)
    
        print("valor a vista: ",x.valor_a_vista())
        print("valor das parcelas: ",x.valor_da_parcela())

UI.main()
