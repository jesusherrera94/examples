#import <nombre librería> as <nombre alias>
import math as mt

codigo = None

# definición de la función
def suma(numero1,numero2):
    resultado = numero1+numero2
    return resultado

def resta(numero1,numero2):
    resultado = numero1-numero2
    print('el resultado de la resta es: ',resultado)

def multiplicar(num1 = 0,num2 = 0):
    resultado = num1*num2
    return resultado

def dividir(num1,num2):
    try:
        resultado = num1/num2
        print('El resultado de la división es: ',resultado)
    except Exception as e:
        print('el resultado es oo')
        print(e)

#funciones que retornan un valor -> return
#funciones que no retornan nada -> no tiene return
while True:
    print('**********************Mi super calculadora***********************\n__________ Menu principal __________')
    codigo = int(input('1.Sumar\n2.Restar\n3.Multiplicar\n4.Dividir\n5.Salir\n6.Potencia\n7.Sigmoidal\nIngrese un número: '))
    #caso de salida
    if(codigo==5):
        break
    if(codigo==1):
        n1 = float(input('ingrese el primer valor: '))
        n2 = float(input('ingrese el segundo valor: '))
        #implementación de la función retornar valores
        resultadoMain = suma(n1,n2)
        print('el resultado de la suma es: ',resultadoMain)
    if(codigo==2):
        n1 = float(input('ingrese el primer valor: '))
        n2 = float(input('ingrese el segundo valor: '))
        #implementación de la función sin retornar valores
        resta(n1,n2)
    if(codigo==3):
        n1 = float(input('ingrese el primer valor: '))
        n2 = float(input('ingrese el segundo valor: '))
        #implementación de la función retornar valores
        resultadoMain = multiplicar(n2)
        print('el resultado de la multiplicación es: ',resultadoMain)
    if(codigo==4):
        n1 = float(input('ingrese el primer valor: '))
        n2 = float(input('ingrese el segundo valor: '))
        dividir(n1,n2)
    print('\n')