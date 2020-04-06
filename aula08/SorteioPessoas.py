#Faça um programa que escreva o nome de 4 pessoas e sorteie uma delas
from random import choice

n1 = str(input("Digite o nome do primeiro participante: "))
n2 = str(input("Digite o nome do segundo participante: "))
n3 = str(input("Digite o nome do terceiro participante: "))
n4 = str(input("Digite o nome do quarto participante: "))

#AVISO: UMA LISTA SEMPRE FICA ENTRE COLCHETES [ ]
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print("O escolhido foi: {}".format(escolhido))