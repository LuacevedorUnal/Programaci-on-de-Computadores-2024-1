def celsius_a_fahrenheit(celsius):
    """Convierte grados Celsius a Fahrenheit."""
    return (celsius * 9/5) + 32

def main():
    while True:
        entrada = input("Ingrese la temperatura en grados Celsius (°C) o 'salir' para terminar: ")
        
        if entrada.lower() == 'salir':
            print("Programa terminado.")
            break
        
        try:
            celsius = float(entrada)
            fahrenheit = celsius_a_fahrenheit(celsius)
            print(f"{celsius:.2f} grados Celsius son {fahrenheit:.2f} grados Fahrenheit.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()