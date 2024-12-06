hora_entrada = int(input('Digite a hora de entrada:'))
minuto_entrada = int(input('Digite o minuto de entrada:'))

hora_saida = int(input('Digite a hora de saída:'))
minuto_saida = int(input('Digite o minuto de saída:'))

entrada_completo = hora_entrada * 60 + minuto_entrada
saida_completo = hora_saida * 60 + minuto_saida

permanencia_completo = saida_completo - entrada_completo
hora_permanencia = permanencia_completo // 60
minuto_permanencia = permanencia_completo % 60


print('O tempo de permanencia foi ', hora_permanencia, 'h', minuto_permanencia)