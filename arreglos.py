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
#C: ArrayChar a = ['c','a','d','e','n','a','s'];
#for(int i i<a.length(); i++){
#     cout<<a[i];
# }
# > cadenas
#qubit -> qubit 1|0 al mismo tiempo

print('Cadenas\n')
#1024 caracteres
#arreglo!
nombre = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat'

#Imprime solo J
print(nombre[9])

#Funciones de búsqueda
#----------- find: devuelve la posicion en la que se encuenta la coincidencia.
print(nombre[ nombre.find('sed') ])

#Imprimir todo el texto
print(nombre)

#funciones de conversion de texto o cadenas
