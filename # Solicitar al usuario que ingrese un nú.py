# Solicitar al usuario que ingrese un número
numero = float(input("Por favor, ingresa un número: "))

# Verificar si el número es positivo, negativo o cero
if numero > 0:
    resultado = "El número es positivo."
elif numero < 0:
    resultado = "El número es negativo."
else:
    resultado = "El número es cero."

# Imprimir el resultado
print(resultado)
2
0