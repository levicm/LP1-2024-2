hora_entrada = int(input("Qual a hora de entrada: "))
minuto_entrada = int(input("Qual o minuto de entrada: "))
qtd_parabrisas = int(input("Informe a quantidade de parabrisas: "))

tempo_por_parabrisa = 1 * 60 + 10
tempo_total_servico = tempo_por_parabrisa * qtd_parabrisas

momento_de_entrada = hora_entrada * 60 + minuto_entrada
momento_de_saida = momento_de_entrada + tempo_total_servico

hora_saida = momento_de_saida // 60
minuto_saida = momento_de_saida % 60

print(f"O carro será liberado às {hora_saida:02d}:{minuto_saida:02d}")
