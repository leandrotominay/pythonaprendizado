# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com sua idade:
# Até 9 Anos: Mirim
# Até 14 anos: Infantil
# Até 19 anos: Junior
# Até 20 anos: Sênior
# Acima: Master
from datetime import date

print("Olá seja bem-vindo ao classificador de atletas por idade!")
ano = int(input('Digite o ano de nascimento do atleta: '))
dataAtual = date.today()
anoAtual = dataAtual.year
idade = anoAtual - ano
print("Ele tem {} anos".format(idade))
if idade >= 0 and idade <= 9:
    print("O Atleta está na Categoria Mirim")

if idade >= 9 and idade <= 14:
    print("O Atleta está na Categoria Infantil")

if idade >= 14 and idade <= 19:
    print("O Atleta está na Categoria Junior")

if idade == 20:
    print("O Atleta está na Categoria Sênior")

if idade > 20:
    print("O Atleta está na Categoria Master")

# OK!