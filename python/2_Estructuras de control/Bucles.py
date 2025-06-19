# Bucles en Python (for, while,)
#Los bucles permiten repetir un bloque de código varias veces, lo que es súper útil para automatizar tareas.

''' 1. while -  Repite mientras una condición sea verdadera
Este bucle verifica la condición antes de ejecutar el código.'''
#sintaxis:
# while condición:
#codigo que se repite

#Ejemplo:|
contador = 1

while contador <= 5:
    print("Número:", contador)
    contador += 1  # Aumenta contador en 1

#2. for – Recorre una secuencia (como una lista o un rango)

# Sintaxis con range():
#for variable in range(inicio, fin):
    # Código que se repite

#Ejemplo:

for i in range(1, 6):
    print("Número:", i)
    #Este también imprime del 1 al 5.

'''Ejercicio práctico
Haz un programa que:

Pida al usuario un número del 1 al 10.

Imprima la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for.'''

numero = int(input("Ingresa un número del 1 al 10: "))

print(f"Tabla del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

