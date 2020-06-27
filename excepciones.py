try:
    n1 = float(input('ingrese el primer valor: '))
    n2 = float(input('ingrese el segundo valor: '))
    resultado = n1/n2
    print('El resultado es: ',resultado)
except Exception as xd:
    print(xd)