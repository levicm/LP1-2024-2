valor_hora = int(input("Qual o valor da hora de trabalho?"))
horas_trabalhadas = int(input("Quantas horas trabalhou no mês?"))

bruto = horas_trabalhadas * valor_hora

ir = (bruto * 11) / 100
inss = (bruto * 8) / 100
sindicato = (bruto * 5) / 100

liquido = bruto - ir - inss - sindicato

print(f"+ Salário Bruto   : R$ {bruto:.2f}")
print(f"- IR (11%)        : R$ {ir:.2f}")
print(f"- INSS (8%)       : R$ {inss:.2f}")
print(f"- Sindicato ( 5%) : R$ {sindicato:.2f}")
print(f"= Salário Liquido : R$ {liquido:.2f}")

