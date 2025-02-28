# Poderia ser feito com uma varredura usando o "for"
def buscar1(numero, numeros):
    encontrou = False
    for numero in numeros:
        if numero == numero_informado:
            encontrou = True
    return encontrou

# Ou poderia ser feito com o operador "in"
def buscar2(numero, numeros):
    return numero in numeros

numeros = [2, 5, 8, 12, 34, 7]

numero_informado = int(input("Digita um número: "))

# Usando diretamente o operador "in"
if numero_informado in numeros:
    print("Número encontrado!")
else:
    print("Número NÃO encontrado!")

