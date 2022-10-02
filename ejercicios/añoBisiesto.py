# 19.- Realice un programa que, dado un año, nos diga si es bisiesto o no. Un año es bisiesto bajo
# las siguientes condiciones: Un año divisible por 4 es bisiesto y no debe ser divisible por 100. Si
# un año es divisible por 100 y además es divisible por 400, también resulta bisiesto.

def añoBisiesto ():
    añoIngresado = int(input(f'ingrese un año por favor: '))
    if (añoIngresado % 4 == 0 and añoIngresado % 100 != 0) or añoIngresado % 400 == 0:
        print(f'el año: {añoIngresado} ingresado es bisiesto')
    else:
        print(f'el año: {añoIngresado} ingresado no es bisiesto')

añoBisiesto()

