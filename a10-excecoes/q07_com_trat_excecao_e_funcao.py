def calcula_imc(altura, peso):
    return peso / (altura ** 2)

def imprimir_faixas_imc():
    print("As faixas do IMC são:")
    print("Peso baixo: até 18,49 kg/m2")
    print("Peso normal: de 18,5 a 24,99 kg/m2")
    print("Peso sobrepeso: de 25 a 29,99 kg/m2")
    print("Peso obesidade: acima de 30 kg/m2")

def situacao_imc(imc):
    if imc < 18.5:
        situacao = "Peso baixo"
    elif imc < 25:
        situacao = "Peso normal"
    elif imc < 29:
        situacao = "Sobrepeso"
    else:
        situacao = "Obesidade"
    return situacao

qtd_sobrepeso = 0
resposta = 'S'
while resposta.upper() == 'S':
    try:
        # Letra a:
        altura = float(input("Informe sua altura (em m): "))
        peso = float(input("Informe seu peso: (em Kg)"))

        # Letra b:
        imc = calcula_imc(altura, peso)
    except ValueError:
        print("Entrada inválida! Por favor, informe números válidos.")
    except ZeroDivisionError:
        print("Impossível calcular! Por favor, informe uma altura maior que zero!")
    else:
        # Letra c:
        print(f"Sem IMC é {imc:.2f}")

        # Letra d:
        imprimir_faixas_imc()

        # Letra e:
        print(f"Você está com {situacao_imc(imc)}")

        if imc >= 25:
            qtd_sobrepeso += 1

    finally:
        resposta = input("Fazer cálculo para outra pessoa [S]im ou [N]ão?")

print("A quantidade de pessoas " \
      f"com sobrepeso ou obesidade (IMC acima de 24,99) é {qtd_sobrepeso}")