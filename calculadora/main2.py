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
    print('\n')