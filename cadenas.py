perros = ['Lucho','Carbon','Kembor','Morgan','Linu','Ivannov','Dante']

#Imprimir todo el arreglo
print('*********Todo el arreglo***********')
print(perros)

#Impresión formateada
#impresion elemento por elemento
for elemento in perros:
    print(elemento)

cadena = ''
for elemento2 in perros:
    #concatenación
    cadena = cadena + elemento2 + ' '
print(cadena)

#Añadir un nuevo elemento
perros.append('cincuenticuatro')
print('*********Todo el arreglo***********')
print(perros)

#Cambiar un objeto por otro
#Actualización del arreglo
nuevoPerro = input('Ingrese el nombre del perro: ')
perros[2] = nuevoPerro
print(perros)

#Busqueda
for item in perros:
    if item == 'Morgan':
        print(item.upper)