



entrada = input("Ingrese hasta 15 números enteros separados por espacios: ")
numeros = list(map(int, entrada.split()))[:15]
cuadrados = list(map(lambda x: x ** 2, numeros))
print("Lista original:", numeros)
print("Lista al cuadrado:", cuadrados)




# # --------------------------------------------------------------------------------------------------------------------------------- #

# def procesar_lista(numeros):
#    if not numeros: 
#        return "La lista está vacía."
#    suma = sum(numeros)
#    maximo = max(numeros)
#    minimo = min(numeros)
#    promedio = suma / len(numeros)
#    return suma, maximo, minimo, promedio
# # Pedir al usuario ingresar los números
# entrada = input("Ingrese hasta 10 números enteros separados por espacios: ")
# numeros = list(map(int, entrada.split()))[:10]  # Convierte a lista de enteros y toma solo 10
# # Llamar a la función y mostrar los resultados
# resultado = procesar_lista(numeros)
# if isinstance(resultado, str):  # Si la lista estaba vacía
#    print(resultado)
# else:
#    suma, maximo, minimo, promedio = resultado
#    print(f"Suma: {suma}")
#    print(f"Número más grande: {maximo}")
#    print(f"Número más pequeño: {minimo}")
#    print(f"Promedio: {promedio:.2f}")

