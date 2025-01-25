valor = int(input("Entre com o valor a ser sacado: "))

cedulas_100 = valor // 100
valor -= (cedulas_100 * 100)

cedulas_50 = valor // 50
valor -= (cedulas_50 * 50)

cedulas_20 = valor // 20
valor -= (cedulas_20 * 20)

cedulas_10 = valor // 10
valor -= (cedulas_10 * 10)

cedulas_2 = valor // 2
valor -= (cedulas_2 * 2)

print(f"{cedulas_100} notas de 100")
print(f"{cedulas_50} notas de 50")
print(f"{cedulas_20} notas de 20")
print(f"{cedulas_10} notas de 10")
print(f"{cedulas_2} notas de 2")