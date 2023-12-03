import numpy as np

# Definir las variables que usaremos para las matrices que darán solución a nuestro circuito

# Definir resistencias tipo float
R1, R2, R3, R4, R5, R6 = float, float, float, float, float, float
# Definir las fuentes
VS1, VS2, VS3 = float, float, float

print("En este código, resolveremos el circuito del parcial #1 de circuitos eléctricos.")
print("Para dar solución al circuito, necesitamos los valores de las resistencias y de los voltajes de las fuentes.")
print("\n")

# Pedir cada dato según el nodo
R1 = float(input("Ingrese el valor de la resistencia (R1) entre los nodos A y B: "))
print("\n")
R2 = float(input("Ingrese el valor de la resistencia entre los nodos (R2) B y E: "))
print("\n")
R3 = float(input("Ingrese el valor de la resistencia entre los nodos (R3) E y G: "))
print("\n")
R4 = float(input("Ingrese el valor de la resistencia entre los nodos (R4) B y C: "))
print("\n")
R5 = float(input("Ingrese el valor de la resistencia entre los nodos (R5) E y F: "))
print("\n")
R6 = float(input("Ingrese el valor de la resistencia entre los nodos (R6) F y H: "))

# Pedir los voltajes
VS1 = float(input("Ingrese el valor de la Fuente #1: "))
VS2 = float(input("Ingrese el valor de la Fuente #2: "))
VS3 = float(input("Ingrese el valor de la Fuente #3: "))

# Realizar las sumas para no realizarlas en la matriz
sumI1 = R1 + R2 + R3
sumI2 = R2 + R4 + R5
sumI3 = R3 + R5 + R6

# Crear la matriz de resistencias de 3x3
matriz_resistencias = np.array([[sumI1, -R2, -R3],
                                [-R2, sumI2, -R5],
                                [-R3, -R5, sumI3]])
# Sacar la inversa a la matriz de resistencias
inversa_matriz_resistencias = np.linalg.inv(matriz_resistencias)
# Crear la matriz de las resistencias 1x3
matriz_fuente = np.array([[VS1, VS2, VS3]])

# Calcular la matriz de corrientes, multiplicar matriz(3x1)*matriz(3x3)
matriz_corrientes = np.dot(matriz_fuente, inversa_matriz_resistencias)

# Imprimir los resultados de manera más explicativa
print("El circuito ha sido resuelto por el método corriente de mallas.")
print("Las corrientes obtenidas son:")
print(f"I1 (malla 1,corriente a través de R1, R2, y R3)-> {round(matriz_corrientes[0, 0], 1)}")
print(f"I2 (malla 2, corriente a través de R2, R4, y R5) -> {round(matriz_corrientes[0, 1], 2)}")
print(f"I3 (malla 3, corriente a través de R3, R5, y R6)-> {round(matriz_corrientes[0, 2], 3)}")
# Imprimir los resultados de manera más explicativa
print("El circuito ha sido resuelto por el método corriente de mallas.")
print("Las corrientes obtenidas son:")
print(f"I1 (malla 1,corriente a través de R1, R2, y R3)-> {matriz_corrientes[0, 0]}")
print(f"I2 (malla 2, corriente a través de R2, R4, y R5) -> {matriz_corrientes[0, 1]}")
print(f"I3 (malla 3, corriente a través de R3, R5, y R6)-> {matriz_corrientes[0, 2]}")

print("Los voltajes de cada resistencia son:")
I1=matriz_corrientes[0,0]
I2=-matriz_corrientes[0,1]
I3=matriz_corrientes[0,2]

print(f"Voltaje Resistencia 1 -> {I1*R1}")
print(f"Voltaje Resistencia 2 ->{(I1-I2)*R2}")
print(f"Voltaje Resistencia 3 ->{(I1-I3)*R3}")
print(f"Voltaje Resistencia 4 ->{I2*R4}")
print(f"Voltaje Resistencia 5 ->{(I2-I3)*R5}")
print(f"Voltaje Resistencia 3 ->{(I3)*R6}")
