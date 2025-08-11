lista_numeros = []
while (True):
    numero = input("Ingrese un número (o 'x' para terminar): ")
    if numero.lower() == 'x':
        break
    try:
        lista_numeros.append(numero)
    except ValueError:
        print("Por favor, ingrese un número válido.")
lista_numeros.sort()
print("Números ordenados:", lista_numeros)
