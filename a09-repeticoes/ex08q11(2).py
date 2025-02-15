
qtd_notas_por_aluno = 2
aprovados = 0
resposta = 's'
while resposta.lower() == 's':
    soma = 0
    for i in range(1, qtd_notas_por_aluno + 1): 
        nota = float(input(f'Informe a nota {i}: '))
        while nota < 0 or nota > 10:
            nota = float(input(f'Nota inválida! Informe novamente a nota {i}: '))
        soma += nota

    media = (soma) / qtd_notas_por_aluno
    print('Média: ', media)
    if media >= 6:
        aprovados = aprovados + 1
    resposta = input('Calcular a média de um outro aluno [S]im ou [N]ão? ')

print("A quantidade de alunos aprovados foi", aprovados)