# Condições Aninhadas
# Se dá o nome aninhada pois parece um ninho, estao uma dentro da outra.
# if condicao1():
# elif condicao2();
# elif condicao3();
# else condicao4();

nome = str(input("Qual é o seu nome? "))
if nome == 'Leandro':
    print("Que nome bonito!")
elif nome == 'Pedro' or nome == "Maria" or nome =="Joao":
    print("Seu nome é bem comum no Brasil!")
elif nome in 'Ana Claudia Jessica Juliana':
    print("É um nome feminino!")
elif nome in 'Yasuo Darius Tryndamere':
    print("Você é um cotoco!")
else:
    print("Seu nome é bem normal..")
print('Tenha um bom dia, {}!'.format(nome))

# OK
