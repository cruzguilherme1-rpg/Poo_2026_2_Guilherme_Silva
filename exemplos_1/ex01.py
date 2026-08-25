class triangulo: 
    def __init__(self):
        self.b=0
        self.h=0
    def calcular_area(self):
        return self.b * self.h /2

x= triangulo()
x.b= 10
x.h= 20
print( x.b, x.h )
print(x.calcular_area())
