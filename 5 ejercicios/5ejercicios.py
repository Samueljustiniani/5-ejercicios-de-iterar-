#ejercicio 1

# Ejemplo de iteración utilizando un bucle for
lista = [1, 2, 3, 4, 5]

for elemento in lista:
    print(elemento)


#ejercicio 2 

# Ejemplo de iteración utilizando la función enumerate
mi_lista = [1, 2, 3, 4, 5]

for indice, valor in enumerate(mi_lista):
    print(f"Índice: {indice}, Valor: {valor}")

#ejercicio 3 

# Ejemplo de iteración utilizando un bucle while
mi_lista = [1, 2, 3, 4, 5]
indice = 2


while indice < len(mi_lista):
    print(mi_lista[indice])
    indice += 1


#ejercicio 4 

# Ejemplo de iteración utilizando comprensión de listas
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nueva_lista = [elemento * 2 for elemento in mi_lista]

print(nueva_lista)

#ejercicio 5 

# Ejemplo de iteración utilizando la función map
mi_lista = [1, 2, 3, 4, 5, 6]

def duplicar(numero):
    return numero * 2
#El uso de map() puede simplificar y hacer más eficiente el proceso de aplicar una función a todos los elementos de una lista sin necesidad de utilizar bucles explícitos.
nueva_lista = list(map(duplicar, mi_lista))

print(nueva_lista)
