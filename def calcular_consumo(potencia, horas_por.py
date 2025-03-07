def calcular_consumo(potencia, horas_por_dia, dias_por_mes):
    """Calcula el consumo de un electrodoméstico en kWh."""
    return (potencia * horas_por_dia * dias_por_mes) / 1000

def obtener_numero(mensaje):
    """Solicita un número al usuario y lo valida."""
    while True:
        try:
            numero = float(input(mensaje))
            if numero < 0:
                print("Por favor, ingrese un número positivo.")
                continue
            return numero
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

def main():
    limite_consumo = 200  # Límite de consumo en kWh
    num_viviendas = int(obtener_numero("¿Cuántas viviendas se quieren analizar? "))

    for i in range(num_viviendas):
        print(f"\n--- Vivienda {i + 1} ---")
        num_electrodomesticos = int(obtener_numero("¿Cuántos electrodomésticos tiene? "))
        
        consumo_total = 0  # Inicializar el consumo total de la vivienda

        for j in range(num_electrodomesticos):
            print(f"\nElectrodoméstico {j + 1}:")
            potencia = obtener_numero("Ingrese la potencia en vatios: ")
            horas_por_dia = obtener_numero("Ingrese las horas de uso al día: ")
            dias_por_mes = obtener_numero("Ingrese los días de uso al mes: ")
            
            consumo = calcular_consumo(potencia, horas_por_dia, dias_por_mes)
            consumo_total += consumo  # Sumar el consumo del electrodoméstico al total

        print(f"\nEl consumo total de la vivienda {i + 1} es: {consumo_total:.2f} kWh")
        
        if consumo_total > limite_consumo:
            print("La vivienda excede el límite permitido de consumo.")
        else:
            print("La vivienda está dentro del límite permitido de consumo.")

if __name__ == "__main__":
    main()