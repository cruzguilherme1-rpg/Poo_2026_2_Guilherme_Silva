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
        else: raise ValueError("Base deve ser positiva")    

    def set_altura(self, v):
        if v >= 0: self.__h = v
        else: raise ValueError("Altura deve ser positiva")

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
        else: raise ValueError("Base deve ser positiva")    

    def set_altura(self, v):
        if v >= 0: self.__h = v
        else: raise ValueError("Altura deve ser positiva")

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
        else: raise ValueError("peso deve ser positiva")    

    def set_distancia(self, v):
        if v >= 0: self.__distancia = v
        else: raise ValueError("distancia deve ser positiva")

    def get_peso(self):
        return self.__peso        

    def get_distancia(self):
        return self.__distancia        

    def calcular_frete(self):
        return f"valor do frete: ", (self.__peso *0.01) * self.__distancia    

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

UI.main()