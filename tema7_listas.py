#listas
lista1 = [10, 5, 3]
lista2 = [1.5, 2.66, 1.70, 89.2]
lista3 = ["Lunes", "Martes", "Miercoles"]
lista4 = ["Juan", 45, 1.92]

print(type(lista1))
print(len(lista1))
print(lista1[0])

suma = 0
x = 0

while x < len(lista1):
    suma = suma + lista1[x]
    x = x + 1
print("La suma es: {}".format(suma))
print(lista1)
print(lista1[0])
lista1.append(100)
print(lista1)
print(lista1[3])

#agregar elementos a la lista
lista5=[]

for x in range(5):
    valor = int (input("Ingresa valor: "))
    lista5.append(valor)
    
print(lista5)

#elementos de la lista
print(lista1)
lista1.pop()
print(lista1)



n = int(input("Introduce la cantidad de numeros: "))

lista_numeros = []

for x in range(n):
    valor = int(input("Ingrese el numero: "))
    lista_numeros.append(valor)
    
print(lista_numeros)

#crear un programa, pedir una cantidad n de numreos y almacenarlos en una lista:
#la salida debera ser la siguiente
#lista completa
#numeros pares
#numeros inpares

n = int(input("Introduce la cantidad de numeros: "))

lista_numeros = []

for x in range(n):
    valor = int(input("Ingrese el numero: "))
    lista_numeros.append(valor)
    
numeros_pares = [num for num in lista_numeros if num % 2 == 0] 
numeros_impares = [num for num in lista_numeros if num % 2 != 0]

print(lista_numeros)
print(numeros_impares)
print(numeros_pares)

#ordenar lista
lista1.sort()
print(lista1)
lista1.reverse()
print(lista1)

lista1.remove(10)
print(lista1)

lista1.clear()
print(lista1)