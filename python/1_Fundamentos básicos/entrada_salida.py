#1. Entrada de Datos: input()
#syntax: 
variable = input("Mensaje al usuario: ")
#Ejemplo:
nombre = input("¿Cuál es tu nombre? ")
print("Hola " + nombre + ", bienvenido al curso de Python")

#2. Convertir la Entrada a Otros Tipos de Datos

#ejemplo
edad = int(input("¿Cuántos años tienes? "))  # Convierte la entrada en un número entero
altura = float(input("¿Cuánto mides en metros? "))  # Convierte la entrada en un número flotante

print("Tu edad es:", edad)
print("Tu altura es:", altura)

#3. Salida de Datos: print()

print("Texto a mostrar")
#Ejemplo:
nombre = "Juan"
edad = 20
nombre = "Juan"
edad = 20
print("Mi nombre es", nombre, "y tengo", edad, "años.")

#4. Formato de Cadenas: f-strings (Python 3.6+)

nombre = "Juan"
edad = 20
print(f"Mi nombre es {nombre} y tengo {edad} años.")


#Ejercicio Práctico

'''Escribe un programa que haga lo siguiente:

Pide al usuario que ingrese su nombre y su edad.

Muestra un mensaje que diga "Hola [nombre], el próximo año tendrás [edad + 1] años."'''
# Entrada de datos
nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuántos años tienes? "))

# Salida de datos
print(f"Hola {nombre}, el próximo año tendrás {edad + 1} años.")

#Ejercicio 2
'''Escribe un programa que haga lo siguiente:
Pide al usuario que ingrese dos números
Muestra la suma de esos dos números.'''
# Entrada de datos
num1 = float(input("Ingresa el primer número: "))       
num2 = float(input("Ingresa el segundo número: "))

resultado = num1 + num2
# Salida de datos   
print(f"La suma de {num1} y {num2} es {resultado}.")



