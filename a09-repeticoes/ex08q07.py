n = int(input('Calcular os divisores de: '))

for i in range(1, n + 1):
    if n % i == 0:
        print(i)