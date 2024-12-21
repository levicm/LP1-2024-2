
resposta = 's'

while resposta.lower() == 's':
    nota1 = float(input('Informe a nota 1: '))
    nota2 = float(input('Informe a nota 2: '))
    print('Média: ', (nota1 + nota2) / 2)
    resposta = input('Calcular a média de um outro aluno [S]im ou [N]ão? ')