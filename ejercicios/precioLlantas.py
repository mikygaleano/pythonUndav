# 18.- Si se compran menos de cinco llantas el precio es de $3000 cada una, si se compran entre 5
# y 10 el precio es de $2500, y si se compran más de 10 el precio es $2000. Obtener la cantidad de
# dinero que una persona tiene que pagar por cada una de las llantas que compra, y el monto total
# que tiene que pagar por el total de la compra.

cantidad = int(input('ingrese la cantidad de llantas deseadas: '))
precio = 0

def precioLlantas ():
    if cantidad < 5:
        precio = 3000
    elif cantidad >= 5 and cantidad <= 10:
        precio = 2500
    else:
        precio = 2000

    def monto ():
        total = precio * cantidad
        print(f'El monto individual de cada llanta es de {precio} y el monto total es de {total} por la cantidad de {cantidad}')

    monto()

precioLlantas()

