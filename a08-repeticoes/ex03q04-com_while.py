"""
Ler um número N qq
Imprimir a tabuada

No caso de ler o nr 5, a tabuada seria:

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 9 = 45
5 x 10 = 50
"""
numero = int(input('Digite um número qualquer: '))

i = 1
while i <= 10:
    print(f'{numero} x {i} =', numero * i)
    i = i + 1

print('Fim!')
