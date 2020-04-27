# Crie um jogo que faça o computador jogar Jokenpô com você.
import random
from time import sleep

print("Olá seja bem-vindo ao Jokenpô!")
print("Pedra = 0")
print("Papel = 1")
print("Tesoura = 2")
escolhaJogador = int(input("Escolha Pedra Papel ou Tesoura: "))
pedra = [0]
papel = [1]
tesoura = [2]
print("Jo..")
sleep(1)
print("Ken..")
sleep(1)
print("POO!")

escolhaComputador = random.randint(0, 2)
if escolhaJogador == 0 and escolhaComputador == 1:
    print("O computador escolheu Papel e venceu, mais sorte na proxima".format(escolhaComputador))
elif escolhaJogador == 0 and escolhaComputador == 2:
    print("O computador escolheu Tesoura e perdeu, parabéns!".format(escolhaComputador))
elif escolhaJogador == 0 and escolhaComputador == 0:
    print("O computador escolheu Pedra e empatou, tente novamente!".format(escolhaComputador))

if escolhaJogador == 1 and escolhaComputador == 2:
    print("O computador escolheu Tesoura e venceu, mais sorte na proxima".format(escolhaComputador))
elif escolhaJogador == 1 and escolhaComputador == 0:
    print("O computador escolheu Pedra e perdeu, parabéns!".format(escolhaComputador))
elif escolhaJogador == 1 and escolhaComputador == 1:
    print("O computador escolheu Papel e empatou, tente novamente!".format(escolhaComputador))

if escolhaJogador == 2 and escolhaComputador == 0:
    print("O computador escolheu Pedra e venceu, mais sorte na proxima".format(escolhaComputador))
elif escolhaJogador == 2 and escolhaComputador == 1:
    print("O computador escolheu Papel e perdeu, parabéns!".format(escolhaComputador))
elif escolhaJogador == 2 and escolhaComputador == 2:
    print("O computador escolheu Tesoura e empatou, tente novamente!".format(escolhaComputador))

# OK

