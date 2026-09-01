class triangulo:
    def __init__(self):
        self.__b= 0 
        self.__h = 0

    def set_base(self, v):
        if v>=0: self.__b = v
        else: raise ValueError("altura deve ser positiva")

    def set_altura(self, v):
            if v>=0: self.__h = v
            else: raise ValueError("altura deve ser positiva")

    def get_base(self):
         return self.__b

    def get_altura(self):
             return self.__h
    

    def calcular_area(self):
        return self.__b * self.__h / 2
class UI:
    @staticmethod
    def main():
        x = triangulo()
        print(x.get_base(), x.get_altura())
        x.set_base(10)
        x.set_altura(20)
        print(x.get_base(), x.get_altura())
        print(x.calcular_area())

UI.main()