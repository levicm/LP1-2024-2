def boas_vindas(lingua):
    if lingua == 'pt':
        return "Olá!"
    elif lingua == 'es':
        return "Hola"
    else:
        return "Hello!"

print(boas_vindas('qq'))
print(boas_vindas('pt'))
print(boas_vindas('es'))