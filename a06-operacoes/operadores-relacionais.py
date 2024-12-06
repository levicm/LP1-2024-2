a = 10
b = 13
c = 3
d = 2

print(a > b)
comp1 = a < b
print(comp1, type(comp1))

tem_dinheiro = True
tem_emprestimo = True
tem_lanche = False

tem_recursos = tem_dinheiro or tem_emprestimo
print("Tem recursos para lanchar?", tem_recursos)

vai_lanchar = tem_recursos and tem_lanche
print("Vai lanchar?", vai_lanchar)
vai_lanchar = (tem_dinheiro or tem_emprestimo) and tem_lanche