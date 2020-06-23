#import <nombre librería> as <nombre alias>
import math as mt

codigo = None

#iniciar con un bloque de repeticion-> NO EXISTE DO-WHILE EN PYTHON
#while(){ sfkhfs.... } cast -> casteo : convertir un dato a otro, por ejemplo letras a números
while True:
    print('**********************Mi super calculadora***********************\n__________ Menu principal __________')
    #int: integer, valor numerico discreto [1,2,3,4,5,6,7,...,+oo]
    #float: float, [1.11,1.12,1.13]
    #double: 1.11111111119, 1.111111111112,......
    codigo = int(input('1.Sumar\n2.Restar\n3.Multiplicar\n4.Dividir\n5.Salir\n6.Potencia\n7.Sigmoidal\nIngrese un número: '))
    if(codigo==5):
        break
    if(codigo==1):
        n1 = float(input('ingrese el primer valor: '))
        n2 = float(input('ingrese el segundo valor: '))
        resultado = n1+n2
        print('el resultado de la multiplicación es: ',resultado)
    if(codigo==2):
        n1 = float(input('ingrese el primer valor: '))
        n2 = float(input('ingrese el segundo valor: '))
        resultado = n1-n2
        print('el resultado de la multiplicación es: ',resultado)
    if(codigo==3):
        n1 = float(input('ingrese el primer valor: '))
        n2 = float(input('ingrese el segundo valor: '))
        resultado = n1*n2
        print('el resultado de la multiplicación es: ',resultado)
    if(codigo==4):
        n1 = float(input('ingrese el primer valor: '))
        n2 = float(input('ingrese el segundo valor: '))
        if(n2!=0):
            resultado = n1/n2
            print('el resultado de la división es: ',resultado)
        else:
            print('el resultado de la división es: oo')
    if(codigo==6):
        n1 = float(input('ingrese el valor de base: '))
        n2 = float(input('ingrese el valor de exponente: '))
        resultado = mt.pow(n1,n2)
        print('el resultado de la división es: ',resultado)
    if(codigo==7):
        expo = float(input('ingrese el valor de exponente: '))
        sigmoidal = 1/(1+mt.exp(-expo))
        print('el resultado de la función es: ',sigmoidal)
    print('\n')