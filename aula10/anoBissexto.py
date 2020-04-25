# Faça um programa que leia um ano qualquer e mostre se ele é bissexto
print("Olá seja bem-vindo ao identificador de ano bissexto!")
ano = int(input("Digite o ano: "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano de {} é bissexto!".format(ano))
else:
    print("O ano de {} não é bissexto!".format(ano))
