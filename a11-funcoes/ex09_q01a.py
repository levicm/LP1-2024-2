titulo = "Tabela de potências"

def imprime_cabecalho():
    print("NUM | QUADRADO | CUBO |")

def imprime_linha(n):
    titulo = "Texto"
    print(titulo)
    print(n, n ** 2, n ** 3)

print(titulo)
for i in range(1, 11):
    imprime_linha(i)
