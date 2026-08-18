a = int(input())
b = int(input())
c = int(input())
d = int(input())

par= 0
impar= 0

if a % 2 == 0:
    par= par+a 
else: 
    impar= impar+a


if b % 2 == 0:
    par= par+b 
else: 
    impar= impar+b


if c % 2 == 0:
    par= par+c
else: 
    impar= impar+c


if d % 2 == 0:
    par= par+d
else: 
    impar= impar+d

print ( "Soma dos pares =",par)
print  ("Soma dos impares=",impar)