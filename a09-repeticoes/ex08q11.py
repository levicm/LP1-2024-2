
resposta = 's'

aprovados = 0
while resposta.lower() == 's':
    nota1 = float(input('Informe a nota 1: '))
    while nota1 < 0 or nota1 > 10:
        nota1 = float(input('Nota inválida! Informe novamente a nota 1: '))

    nota2 = float(input('Informe a nota 2: '))
    while nota2 < 0 or nota2 > 10:
        nota2 = float(input('Nota inválida! Informe novamente a nota 2: '))

    media = (nota1 + nota2) / 2
    print('Média: ', media)
    if media >= 6:
        aprovados = aprovados + 1
    resposta = input('Calcular a média de um outro aluno [S]im ou [N]ão? ')

print("A quantidade de alunos aprovados foi", aprovados)