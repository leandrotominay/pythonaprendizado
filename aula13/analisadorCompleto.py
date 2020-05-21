# Desenvolva um programa que leia nome idade e sexo de quatro pessoas
# no final o programa deve mostrar a média de idade do grupo, o nome do homem mais velho
# e quantas mulheres tem menos de 20 anos.
from datetime import date
atual = date.today().year
somaidade = 0
maioridadehomem = 0
nomevelho = ''
mulhernova = 0

for p in range(1, 4+1):
    print('------- {} pessoa -------'.format(p))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    if p == 1 and sexo in 'fF':
        menoridademulher = idade
    if sexo in 'fF' and idade < 20:
        mulhernova += 1
mediaidade = somaidade / 4
print("A média de idade do grupo é igual a {}".format(mediaidade))
print("O Homem mais velho se chama {} e tem {} anos.".format(nomevelho, maioridadehomem))
print("São {} mulheres com menos de 20 anos.".format(mulhernova))
