print("-"*30)
#1. Operadores Aritméticos
a = 10
b = 5

# Suma
suma = a + b  # Resultado: 15

# Resta
resta = a - b  # Resultado: 5

# Multiplicación
multiplicacion = a * b  # Resultado: 50

# División
division = a / b  # Resultado: 2.0 (siempre será un float)

# División entera
division_entera = a // b  # Resultado: 2 (solo la parte entera de la división)

# Módulo (resto de la división)
modulo = a % b  # Resultado: 0 (resto de la división)

# Exponente
exponente = a ** b  # Resultado: 100000 (10 elevado a 5)
print("-"*30)
#2. Operadores Relacionales
a = 10
b = 5

# Igual a
print(a == b)  # False (10 no es igual a 5)

# Diferente de
print(a != b)  # True (10 es diferente de 5)

# Mayor que
print(a > b)  # True (10 es mayor que 5)

# Menor que
print(a < b)  # False (10 no es menor que 5)

# Mayor o igual que
print(a >= b)  # True (10 es mayor o igual que 5)

# Menor o igual que
print(a <= b)  # False (10 no es menor o igual que 5)

#3. Operadores Lógicos
a = True
b = False

# AND (Y lógico)
print(a and b)  # False (ambas deben ser True para que el resultado sea True)

# OR (O lógico)
print(a or b)  # True (al menos uno debe ser True para que el resultado sea True)

# NOT (Negación)
print(not a)  # False (invierte el valor de la expresión)

#4. Operadores de Asignación
a = 10
a += 5  # a = a + 5 (ahora a es 15)
a -= 3  # a = a - 3 (ahora a es 12)
a *= 2  # a = a * 2 (ahora a es 24)
a /= 4  # a = a / 4 (ahora a es 6.0)
a //= 2  # a = a // 2 (ahora a es 3.0)
a %= 2  # a = a % 2 (ahora a es 1.0)
a **= 3  # a = a ** 3 (ahora a es 1.0, ya que 1 elevado a cualquier número es 1)

#5. Operadores de Identidad
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)  # True (y es el mismo objeto que x)
print(x is z)  # False (x y z son objetos diferentes aunque tengan el mismo valor)
print(x == z)  # True (los valores de x y z son iguales)
print(x is not z)  # True (x y z son objetos diferentes)
print(x is not y)  # False (x y y son el mismo objeto)

#6. Operadores de Membresía

# Comprobando en una lista
lista = [1, 2, 3, 4, 5]
print(3 in lista)  # True (3 está en la lista)
print(6 not in lista)  # True (6 no está en la lista)


#ejercicio 
'''Define dos números en el código (como enteros).

Realiza la suma, la resta y la multiplicación de esos dos números.

Compara esos dos números usando operadores relacionales.'''


# Definir dos números
numero1 = 8
numero2 = 4

# Suma, resta y multiplicación
print("Suma:", numero1 + numero2)
print("Resta:", numero1 - numero2)
print("Multiplicación:", numero1 * numero2)

# Comparaciones
print("¿Es el primer número igual al segundo?", numero1 == numero2)
print("¿Es el primer número mayor que el segundo?", numero1 > numero2)
print("¿Es el primer número menor que el segundo?", numero1 < numero2)
print("¿Es el primer número diferente al segundo?", numero1 != numero2)
print("¿Es el primer número mayor o igual que el segundo?", numero1 >= numero2)
print("¿Es el primer número menor o igual que el segundo?", numero1 <= numero2)

