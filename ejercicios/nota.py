# 20.- Escriba un programa que valide si una nota está entre 0 y 10, sino está entre 0 y 10 la nota
# se pedirá de nuevo hasta que la nota sea correcta.

nota = int(input(f'Ingrese la nota, por favor: '))


i = 0
while nota < 0 or nota > 10:
    print(f'Nota {nota} invalida')
    nota = int(input('Por favor vuelva a ingresar una nota valida: '))
    i =+ 1
    j = 0
    while nota >= 0 and nota <= 10:
        print(f'Nota {nota} valida')
        j += 1
        break



    

    






