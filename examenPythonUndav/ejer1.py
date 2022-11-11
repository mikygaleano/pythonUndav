# crea una lista de 100 posiciones con numeros aleatorios. Mostrar el numero minimo
# maximo, si contiene el numero 10, indicarle al usuario que lo contiene y la cantidad
#  de veces que aparece. 

import random

# variables

x = range(0, 100,)
listaNumeros = []
repetido = 0


# funciones

def lista ():
	repetido = 0
	for i in x:
		listaNumeros.append(i)
	for i in listaNumeros:
		listaNumeros[i] += random.randint(1, 10)
		if listaNumeros[i] == 10:
			repetido = repetido + 1
	print(listaNumeros)
	print(f'Contiene el Nª10, {repetido} veces')
		

def maximoMinimo ():
	print(f'El Nª maximo es {max(listaNumeros)}')	
	print(f'El Nª minimo es {min(listaNumeros)}')

# llamado



lista()
maximoMinimo()