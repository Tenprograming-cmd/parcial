# suma = 0  # Inicializar la variable fuera del bucle

# for i in range(2, 11, 2):  # Itera desde 2 hasta 10 con paso de 2
#     suma +=1  # Acumula la suma en cada iteración
#     print(suma)  # Muestra el resultado final 

# suma = 0  # Inicializar la variable fuera del bucle

# for i in range(2, 11, 2):  # Itera desde 2 hasta 10 con paso de 2
#     print(suma)  # Muestra el resultado final 
#     suma +=i  # Acumula la suma en cada iteración

# def suma(a, b):
#     return a + b

# resultado = suma(5, 3)
# print("La suma es:", resultado)

def procesar_lista(numeros):
    if not numeros:
        return "la lista esta vacia. "
    suma=sum(numeros) 
    maximo=max(numeros) 
    minimo=min(numeros) 
    promedio=suma/len(numeros) 
    return suma,maximo,minimo,promedio

entrada=int(input("ingrese  hasta 10 numeros enteros "))
numero=list(map())


#-----------------------------------------------------------------------





