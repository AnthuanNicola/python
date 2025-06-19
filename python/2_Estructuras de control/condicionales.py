#Condicionales (if, else, elif,)

# 1. if (si)

edad = 18

if edad >= 18:
    print("Eres mayor de edad")

#2. else (sino)

edad = 16

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#3. elif (sino si)

nota = 15

if nota >= 18:
    print("Excelente")
elif nota >= 14:
    print("Bien")
else:
    print("Necesitas mejorar")


#Operadores que puedes usar en condiciones:
# == (igual), != (diferente), > (mayor), < (menor), >= (mayor o igual), <= (menor o igual)
# and (y), or (o), not (no)


''' Ejercicio Práctico
Crea un programa que:

Pida una nota del 0 al 20.

Si la nota es mayor o igual a 18 → “Excelente”

Si la nota está entre 14 y 17 → “Bien hecho”

Si está entre 11 y 13 → “Suficiente”

Si es menor a 11 → “Reprobado”'''

nota = int(input("Ingresa tu nota (0-20): "))

if nota >= 18:
    print("Excelente")
elif nota >= 14:
    print("Bien hecho")
elif nota >= 11:
    print("Suficiente")
else:
    print("Reprobado")

