# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1. O nome com todas as letras maiusculas
# 2. O nome com todas as letras minusculas
# 3. Quantas letras ao total (sem considerar os espaços)
# 4. Quantas letras tem no primeiro nome

nome = str(input("Digite o seu nome completo: ")).strip()

print("Olá {}, Seja bem-vindo ao leitor de nome.".format(nome.title()))

print("O Seu nome com letras maiusculas: {}".format(nome.upper()))


print("O Seu nome com letras minusculas: {}".format(nome.lower()))

print("Quantas letras há no seu nome completo: {}".format(len(nome) - nome.count(' '))) # 21
print("Seu primeiro nome tem {} letras.".format(nome.find(' ')))


