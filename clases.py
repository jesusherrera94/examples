#clases -> class
class HolaMundo:
    #Dentro de si, tienen un constructor.
    def __init__(self,nombre):
        #Nombres de variables globales
        #Nombres de ATRIBUTOS
        self.nombre = nombre
    def saludo(self):
        print('Hola mundo desde clase!',self.nombre)

#Instancia de clase(creación de objetos)
xd = input('Ingrese un nombre: ')

holaMundo = HolaMundo(xd)

hw2 = HolaMundo('Chungy')
#Ejecutar funciones de clases

holaMundo.saludo()

hw2.saludo()