lista = ["Aracaju", "Areia Branca", "Itabaiana"]
print(lista)
print("Tamanho: ", len(lista))

for cidade in lista:
    print(cidade)

for i in range(len(lista)):
    print(i + 1, " - ", lista[i])

print("------")
for i, cidade in enumerate(lista):
    print(i + 1, " - ", cidade)

lista2 = lista

lista2.append("Frei Paulo")
lista2[2] = "Propriá"

print("------")
print(lista)
print(lista2)

lista2 = lista[1:3]

print("------")
print(lista)
print(lista2)

lista2 = lista[:]

print("------")
print(lista)
print(lista2)

lista2.insert(1, "Barra")

print("------")
print(lista)
print(lista2)

lista3 = lista + lista2

print("------")
print(lista)
print(lista2)
print(lista3)

print("------")
if "Barra" in lista:
    print("Posicao da Barra na lista:", lista.index("Barra"))

if "Barra" in lista2:
    print("Posicao da Barra na lista2:", lista2.index("Barra"))

lista.remove("Barra")