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
        print("1 - Frete, 9 - Fim")
        return int(input("Escolha uma opção: "))    
    @staticmethod
    def main():    
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.frete()
    
    @staticmethod
    def frete():
        KG = float(input("informe o peso do pedido: ")) 
        KM = float(input("informe a distancia do pedido: "))
        x = Frete(KG,KM)
        print(x)
        print(x.calcular_frete())

UI.main()