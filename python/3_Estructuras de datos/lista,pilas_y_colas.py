#listas 
''' Una lista en Python es como una colección de datos ordenados, donde puedes agregar, quitar, y acceder a elementos fácilmente. '''
frutas = ["manzana", "pera", "uva"]
print(frutas[0])  # manzana

#pilas(Stack)
''' Operaciones:
append() ➝ agrega un elemento al final (como "empujar")

pop() ➝ quita el último elemento (como "sacar") '''
pila = []

pila.append("A")  # push
pila.append("B")
pila.append("C")

print(pila)        # ['A', 'B', 'C']
print(pila.pop())  # Quita 'C'
print(pila)        # ['A', 'B']

# 3. Colas (Queue)
''' Para colas, usamos collections.deque que es más rápido y eficiente: '''
from collections import deque

cola = deque()

cola.append("persona 1")  # entra primero
cola.append("persona 2")
cola.append("persona 3")

print(cola)           # deque(['persona 1', 'persona 2', 'persona 3'])
print(cola.popleft()) # sale 'persona 1'
print(cola)           # deque(['persona 2', 'persona 3'])

#practica 
from collections import deque

cola_tareas = deque()

cola_tareas.append("Tarea 1")
cola_tareas.append("Tarea 2")
cola_tareas.append("Tarea 3")

while cola_tareas:
    tarea = cola_tareas.popleft()
    print("Ejecutando:", tarea)
