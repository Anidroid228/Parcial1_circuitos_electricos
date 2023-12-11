# Asignación de valores de resistencias y voltajes
r1 = float(input("Ingrese el valor de R1: "))
r2 = float(input("Ingrese el valor de R2: "))
r3 = float(input("Ingrese el valor de R3: "))
r4 = float(input("Ingrese el valor de R4: "))
r5 = float(input("Ingrese el valor de R5: "))
r6 = float(input("Ingrese el valor de R6: "))

Va = float(input("Ingrese el valor de Va: "))
Vb = float(input("Ingrese el valor de Vb: "))
Vc = float(input("Ingrese el valor de Vc: "))

# Cálculo del determinante
determinante = (r1 + r2 + r3) * ((r2 + r4 + r5) * (r3 + r5 + r6) - (-r5) ** 2) - (-r2) * ((-r2) * (r3 + r5 + r6) - (-r5) * (-r3)) + \
               ((-r2) * (-r5) - (r2 + r4 + r5) * (-r3))

# Cálculo de i1
i1 = ((Va) * ((r2 + r4 + r5) * (r3 + r5 + r6) - (-r5) ** 2) - (-Vb) * ((-r2) * (r3 + r5 + r6) - (-r3) * (-r5)) + (Vc) * ((-r2) * (-r5) - (-r3) * (r2 + r4 + r5))) / determinante

# Cálculo de i2
i2 = ((r1 + r2 + r3) * ((-Vb) * (r3 + r5 + r6) - (-r5) * (Vc)) - (Va) * ((-r2) * (r3 + r5 + r6) - (-r5) * (-r3)) + (-r3) * ((-r2) * (Vc) - (-r3) * (-Vb))) / determinante

# Cálculo de i3
i3 = ((r1 + r2 + r3) * ((r2 + r4 + r5) * (Vc) - (-Vb) * (-r5)) - (-r2) * ((-r2) * (Vc) - (-r3) * (-Vb)) + (Va) * ((-r2) * (-r5) - (r2 + r4 + r5) * (-r3))) / determinante

# Imprimir los resultados
print("Determinante:", determinante)
print("i1:", i1)
print("i2:", i2)
print("i3:", i3)

