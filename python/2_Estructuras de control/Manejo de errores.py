#Manejo de errores en Python (try, except, finally)
''' ¿Qué es?
A veces ocurren errores al ejecutar un programa, como cuando el usuario escribe texto en lugar de un número.
El manejo de errores permite prevenir que el programa se detenga de golpe y mostrar mensajes más claros.'''

#1. try y except
'''try: Intenta ejecutar un bloque de código.

except: Si hay un error en el try, ejecuta este bloque en su lugar.'''

#Ejemplo 

try:
    numero = int(input("Ingresa un número: "))
    print("El número ingresado es:", numero)
except:
    print("¡Eso no es un número válido!")

#2. finally
'''Este bloque se ejecuta siempre, haya error o no.
Sirve para limpiar recursos, cerrar archivos, mostrar mensajes finales, etc.'''
#Ejemplo
try:
    numero = int(input("Ingresa un número: "))
    print("Todo salió bien.")
except:
    print("¡Error! No ingresaste un número.")
finally:
    print("Fin del programa.")


''' 3. Capturar tipos específicos de errores
Puedes especificar qué tipo de error quieres manejar:'''

try:
    numero = int(input("Ingresa un número entero: "))
except ValueError:
    print("¡Debes ingresar solo números!")

'''Ejercicio práctico
Crea un programa que:

Pida dos números.

Los divida.

Maneje los errores de:

División por cero.

Entrada inválida (texto en vez de número).'''
try:
    a = float(input("Ingresa el numerador: "))
    b = float(input("Ingresa el denominador: "))
    resultado = a / b
    print(f"Resultado: {resultado}")
except ValueError:
    print("Por favor, ingresa solo números.")
except ZeroDivisionError:
    print("No se puede dividir entre cero.")
finally:
    print("Operación finalizada.")
