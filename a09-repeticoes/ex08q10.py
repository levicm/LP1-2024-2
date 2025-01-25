
resposta = 's'

aprovados = 0
while resposta.lower() == 's':
    nota1 = float(input('Informe a nota 1: '))
    nota2 = float(input('Informe a nota 2: '))
    media = (nota1 + nota2) / 2
    print('Média: ', media)
    if media >= 6:
        aprovados = aprovados + 1
    resposta = input('Calcular a média de um outro aluno [S]im ou [N]ão? ')

print("A quantidade de alunos aprovados foi", aprovados)