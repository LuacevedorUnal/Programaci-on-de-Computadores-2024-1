import math

def calcular_trayectoria(v0, angulo, delta_t):
    angulo_rad = math.radians(angulo)
    v0x = v0 * math.cos(angulo_rad)
    v0y = v0 * math.sin(angulo_rad)
    g = 9.81
    
    tiempo = 0.0
    x, y = 0.0, 0.0
    trayectoria = []
    
    while y >= 0:
        trayectoria.append((tiempo, (round(x, 2), round(y, 2))))
        tiempo += delta_t
        x = v0x * tiempo
        y = v0y * tiempo - 0.5 * g * tiempo**2
    
    return trayectoria

# Ejemplo de uso
velocidad_inicial = 30
angulo = 45
delta_t = 0.1

trayectoria = calcular_trayectoria(velocidad_inicial, angulo, delta_t)
for tiempo, (x, y) in trayectoria:
    print(f"Tiempo: {tiempo}s | Posición: ({x}, {y})")
print(f"El proyectil tocó el suelo después de {trayectoria[-1][0]} segundos.")