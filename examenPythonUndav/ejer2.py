# el usuario ingresa una frase y se carga en una lista. Se muestra
# la lista con las vocales, cambiadas por @

# variables

lista = []

# funciones
def funcion ():
    frase = input('Ingrese una frase: ')
    frase.lower()
    lista.append(frase)
    for i in lista:
        if i == 'a':
            i = '@'
        elif i == 'e':
            i = '@'
        elif i == 'i':
            i = '@'
        elif i == 'o':
            i = '@'
        elif i == 'u':
            i = '@'
    print(i)

# llamado
funcion()