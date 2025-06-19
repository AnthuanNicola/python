#1. Arreglo Unidimensional (una lista común)
edades = [12, 15, 17, 20]
for edad in edades:
    print(edad)

#2. Arreglo Bidimensional (matriz)
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
