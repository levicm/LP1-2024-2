qtd_notas_por_aluno = 2

def pega_nota(i):
    valido = False
    while not valido:
        try :
            nota = float(input(f'Informe a nota {i}: '))
            if (nota < 0 or nota > 10):
                print("Valor inválido! Informe um valor entre 0 e 10!")
            else:
                valido = True
        except ValueError:
            print("Valor inválido! Informe um valor numérico!")
    return nota

def pega_media():
    soma = 0
    for i in range(1, qtd_notas_por_aluno + 1): 
        nota = pega_nota(i)
        soma += nota

    media = (soma) / qtd_notas_por_aluno
    return media


aprovados = 0
resposta = 's'
while resposta.lower() == 's':
    media = pega_media()
    print('Média: ', media)
    if media >= 6:
        aprovados = aprovados + 1
    resposta = input('Calcular a média de um outro aluno [S]im ou [N]ão? ')

print("A quantidade de alunos aprovados foi", aprovados)