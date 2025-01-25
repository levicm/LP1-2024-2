n = int(input('Entre com um numero qualquer: '))

qtd_divisores = 0
for i in range(1, n + 1):
    if n % i == 0:
        qtd_divisores += 1

print(qtd_divisores)

if qtd_divisores == 2:
    print(f"O numero {n} é primo!")
else:
    print(f"O numero {n} NÃO é primo!")