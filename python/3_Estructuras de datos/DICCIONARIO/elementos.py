'''2. Elementos de acceso en diccionarios de Python
Cuando tienes un diccionario, puedes acceder al valor de una clave específica usando corchetes [] o el método .get().'''

mi_diccionario = {
    "nombre": "Carlos",
    "edad": 25,
    "ciudad": "Arequipa"
}

#Acceder con corchetes []
print(mi_diccionario["nombre"])  # Salida: Carlos
print(mi_diccionario["edad"])    # Salida: 25


#Acceder con .get()
print(mi_diccionario.get("nombre"))      # Salida: Carlos
print(mi_diccionario.get("profesion"))   # Salida: None (no error)


#También puedes darle un valor por defecto si no existe:
print(mi_diccionario.get("profesion", "No especificado"))  # Salida: No especificado
