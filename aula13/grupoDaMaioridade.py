# Crie um programa que leia o ano de nascimento de 7 pessoas, no final mostre quantas ainda não atingiram a maioridade
# e quantas já são maiores.
from datetime import date

atual = date.today().year
contmaior = 0
contmenor = 0

for c in range(1, 7+1):
    ano = int(input("Em que ano a {} pessoa nasceu ?: ".format(c)))
    idade = atual - ano
    if idade <= 18:
        contmaior += 1
    elif idade >= 18:
        contmenor += 1

print("{} pessoas são maiores de idade.".format(contmaior))
print("{} pessoas são menores de idade".format(contmenor))

