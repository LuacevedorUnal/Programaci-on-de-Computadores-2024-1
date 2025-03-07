def calcular_inversion(C, r, t, n, D):
    if r < 0 or C < 0 or D < 0:
        raise ValueError("Los valores deben ser positivos.")
    
    r_decimal = r / 100
    total = C
    evolucion = []
    
    for año in range(1, t + 1):
        for _ in range(n):
            total = total * (1 + r_decimal / n) + D
        evolucion.append((año, round(total, 2)))
    
    return evolucion

# Ejemplo de uso
capital_inicial = 5000
tasa_interes = 5
años = 10
frecuencia = 12
deposito = 200

resultado = calcular_inversion(capital_inicial, tasa_interes, años, frecuencia, deposito)
for año, total in resultado:
    print(f"Año {año}: ${total}")
print(f"Total después de {años} años: ${resultado[-1][1]}")