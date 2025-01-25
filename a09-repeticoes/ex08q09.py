qtd = 10

maior = 0
menor = 1000
soma_altura_mulheres = 0
qtd_mulheres = 0
qtd_homens = 0

print(f"Informe os dados de {qtd} pessoas:")
for i in range(1, qtd + 1):
    sexo = input("Entre com o sexo ('M'asculino/'F'eminino) [M/F]: ")
    altura = int(input("Entre com a altura (em cm): "))

    if altura > maior:
        maior = altura

    if altura < menor:
        menor = altura

    if (sexo == "F"):
        qtd_mulheres += 1
        soma_altura_mulheres += altura
    else:
        qtd_homens += 1

media_altura_mulheres = soma_altura_mulheres / qtd_mulheres
print(f"(i) a maior altura foi {maior} e a menor altura foi {menor};")
print(f"(ii) a média de altura das mulheres foi {media_altura_mulheres};")
print(f"e (iii) o número de homens foi {qtd_homens}.")
