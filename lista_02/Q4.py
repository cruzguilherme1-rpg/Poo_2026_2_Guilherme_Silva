dia= int(input())
mes= int(input())
ano= int(input())

if dia <0 or dia>31:
    print("data invalida")

    if mes <0 or mes > 12:
        print("data invalida")

        if ano < 1900 or ano >2100:
            print("data invalida")
else:
    print( dia,"/",mes,"/",ano,"é uma data valida" )


