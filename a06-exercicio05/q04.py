"""
Tendo como dados de entrada a altura de uma pessoa, construa 
um algoritmo que calcule seu peso ideal, usando a seguinte 
fórmula: (72.7*altura) - 58
"""
altura = float(input("Entre com sua altura (em metros): "))

peso_ideal = (72.7 * altura) - 58

print("Seu peso ideal é ", peso_ideal, "Kg")