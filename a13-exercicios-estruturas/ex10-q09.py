pessoas = [
  {"nome": "Levi", "sobrenome": "Mota" },
  {"nome": "João", "sobrenome": "Silva" },
  {"NOME": "Sabriny", "SOBRENOME": "Dantas" },
  {"nome": "Douglas", "sobrenome": "Andrade" },
] 

print(pessoas)

# Faz inicialmente o tratamento para os casos em que as chaves estão em mauísculas
for pessoa in pessoas:
    if not pessoa.get("nome"):
        pessoa["nome"] = pessoa.get("NOME")
        pessoa["sobrenome"] = pessoa.get("SOBRENOME")
        del pessoa["NOME"]
        del pessoa["SOBRENOME"]

print(pessoas)

print("Referências:")
for pessoa in pessoas:
    print(f"Autor: {pessoa.get("sobrenome")}, {pessoa.get("nome")}")