n = int(input('Calcular o fatoria de: '))

fatorial = 1
for i in range(2, n + 1):
    fatorial = fatorial * i

print(f"O fatorial de {n} é {fatorial}")