def detectPalindromo(textToTest):
    textReverse = ""
    #por ejemplo si, el tamaño del texto es 10, el range iria de 1 a 11
    for i in range(1, len(textToTest) + 1):
        #En el primer ciclo sería, 10-1=9, que es el número de la última posición de ese arreglo.
        #así sucesivamente hasta llegar a 10-10=0 que es la primer posición del arreglo original.
        #cuando llega a 11 no entra porque el range es como decir 10<11, si, 11<11, no porque no entra al igual.
        textReverse += textToTest[len(textToTest) - i]
    
    if(textReverse.lower()==textToTest.lower()):
        print('Es palindromo')
    else:
        print('No es palindromo')

#codigo del programa
text = input('Ingrese un texto: ')
detectPalindromo(text)
