'''bucles while'''
'''i = 1#se crea una variable llamada contador y se le da el valor inicual 1
while i < 6:#minetras el valor de contador sea menor  a 5
  print(i)#muestra el valor actual de contador
  i += 1#suma 1 a la variable contador(equivale a contador = contador +1)'''
  
  
'''practica'''
'''clave = ""
while clave !="1234":
      clave =input("introduce la contraseña") #se pide al usuario que escriba algo
print("¡contraseña correcta")''' 

'''ddeclaracion de break'''
#Con la instrucción break podemos detener el bucle incluso si el while condition es true:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1