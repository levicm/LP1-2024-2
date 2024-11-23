x = input('Digite o valor de X: ')
y = input('Digite o valor de y: ')

print('Trocando os valores da maneira tradicional...')
temp = y
y = x
x = temp

print('x:', x, '. y:', y)

print('Trocando os valores usando atribuição múltipla')
y, x = x, y

print('x:', x, '. y:', y)