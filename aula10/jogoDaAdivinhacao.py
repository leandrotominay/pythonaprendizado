# Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 a 5
# e peça para o usuário tentar descobrir qual foi o numero escolhido pelo computador.
# o programa deverá escrever na tela se o usuário ganhou ou perdeu.

from random import randint

print("Bem-vindo ao Jogo da Adivinhação")
pronto = str(input("Eu irei pensar em um número e você deverá adivinha-lo, você está pronto? s/n"))
pronto = pronto.upper()
if pronto == "S":
    print("Ok, agora tente adivinhar o número que eu estou pensando")
    num = randint(0,5)
    type = input("Diga qual numero eu estou pensando: ")
    if type == num:
        print("Você acertou!")
    else:
        print("Você errou! eu estava pensando no número {}".format(num))
else:
    print("Até uma próxima vez!")