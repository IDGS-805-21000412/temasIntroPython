#pedir dos puntos
#calcular la distancia entre esos dos puntos

#commit 
#dia 16 enero archivos

from math import sqrt

print("Ingresa los valores del punto 1 (x1 y y1): ")
x1 = float(input())
y1 = float(input())

print("Ingresa los valores del punto 2 (x2 y y2): ")
x2 = float(input())
y2 = float(input())

distancia = sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"La distancia entre los dos puntos es: {distancia}")