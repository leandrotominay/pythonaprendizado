# Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 a 10
# e peça para o usuário tentar descobrir qual foi o numero escolhido pelo computador.
# o programa deverá rodar até que o jogador acerte, mostrando no
# final quantos palpites foram necessarios para vencer.
from random import randint
numero = randint(1, 10)
palpite = 1

print("-=-=- Bem-vindo ao jogo de Adivinhação -=-=-=")
print("Eu pensei em um numero, agora tente adivinhar qual é!")
chute = int(input("Digite um numero: "))
while chute != numero:
    palpite += 1
    chute = int(input("Você errou! tente novamente: "))
print("Parabéns! depois de {} tentativas você finalmente me venceu!".format(palpite))

