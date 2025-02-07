qtd_sobrepeso = 0
resposta = 'S'
while resposta.upper() == 'S':
    # Letra a:
    altura = float(input("Informe sua altura (em m): "))
    peso = float(input("Informe seu peso: (em Kg)"))

    # Letra b:
    imc = peso / (altura ** 2)

    # Letra c:
    print(f"Sem IMC é {imc:.2f}")

    # Letra d:
    print("As faixas do IMC são:")
    print("Peso baixo: até 18,49 kg/m2")
    print("Peso normal: de 18,5 a 24,99 kg/m2")
    print("Peso sobrepeso: de 25 a 29,99 kg/m2")
    print("Peso obesidade: acima de 30 kg/m2")

    # Letra e:
    if imc < 18.5:
        situacao = "Peso baixo"
    elif imc < 25:
        situacao = "Peso normal"
    elif imc < 29:
        situacao = "Sobrepeso"
    else:
        situacao = "Obesidade"

    if imc >= 25:
        qtd_sobrepeso += 1


    print(f"Você está com {situacao}")

    resposta = input("Fazer cálculo para outra pessoa [S]im ou [N]ão?")

print("A quantidade de pessoas " \
      f"com sobrepeso ou obesidade (IMC acima de 24,99) é {qtd_sobrepeso}")