nombres =  ['Dania','Chungy','Pedro','José','Martha','Ana','Fer','Javier','María','Sophia']
#editar el valor de un arreglo
nombres[3]='Estefanía'
#Añadir un valor al arreglo de nombres
nombres.append('José')
#Eliminar el último valor
print(nombres[nombres.__len__()-1])
print('La dimension del arreglo es: ',nombres.__len__())

#for y arreglos
listNumber = [4,7,5,8,45,8]

#for
#sintaxis: for <item en singular> in <nombre del arreglo>:
#foreach
for peakyBlinder in nombres:
    if(peakyBlinder=='Estefanía'):
        print(peakyBlinder)


#Cadenas
#Las cadenas(textos) son un tipo especial de areglos.

print('Cadenas\n')
nombre = 'Juan Perez'

#Imprime solo J
print(nombre[0])



