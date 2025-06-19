#variable
# En Python, las variables se crean al asignar un valor a un nombre de variable

nombre = "Juan"  # La variable 'nombre' almacena la cadena "Juan"
edad = 25  # La variable 'edad' almacena el número 25

print("Hola, " + nombre + ". Tienes " + edad + " años.")

# Constante
# En Python, no hay una forma nativa de declarar constantes,
# pero se puede usar una convención de nombres en mayúsculas
PI = 3.1416  # El valor de PI no cambiará en el programa
print("El valor de PI es: " + PI)

#Buenas prácticas para nombrar variables y constantes

'''Para variables:
Los nombres de las variables deben ser significativos, es decir, deben 
describir el valor que almacenan.

En Python, se recomienda usar snake_case (todo en minúsculas y 
separando las palabras con guiones bajos) para las variables.'''

nombre_usuario = "Juan"
edad_usuario = 25
altura_usuario = 1.75

'''Para constantes:
Los nombres de las constantes deben estar en mayúsculas y,
si son nombres compuestos, se separan con guiones bajos.'''

MAXIMO_INTENTO = 5
TAMANO_PANTALLA = 1920
ANCHO = 1080

#Ejercicio Práctico

'''Escribe un programa que haga lo siguiente:

Define una variable para tu nombre, una para tu edad, y otra para tu ciudad.

Define una constante para la cantidad máxima de intentos para acceder a una cuenta.

Muestra el contenido de todas las variables y la constante.

Ejemplo de código:'''

# Definir variables
nombre = "Carlos"
edad = 28
ciudad = "Madrid"

# Definir constante
MAXIMO_INTENTOS = 3

# Mostrar las variables y la constante
print("Nombre:", nombre)
print("Edad:", edad)
print("Ciudad:", ciudad)
print("Máximo de intentos:", MAXIMO_INTENTOS)
