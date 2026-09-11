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
    

class UI:
    @staticmethod
    def menu():
        print("1 - Retângulo, 9 - Fim")
        return int(input("Escolha uma opção: "))    
    @staticmethod
    def main():    
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.retangulo()
    
    @staticmethod
    def retangulo():
        b = float(input("informe a base do retangulo")) 
        h = float(input("informe a altura do retangulo"))
        x = Retangulo(b,h)
        print(x)
        print(x.calcular_area())
        print(x.calcdiaonal())

UI.main()