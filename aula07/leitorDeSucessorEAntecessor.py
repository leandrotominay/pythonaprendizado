import math
#Faça um programa que leia um número inteiro
#e mostre na tela o seu sucessor e seu antecessor
print("**Programa que le numero inteiro e exibe sucessor e antecessor**")
number = int(input('Digite um numero: '))
ant = number - 1
suc = number + 1
print('O Antecessor do numero {} é igual a {}, e o seu Sucessor é {}.'.format(number, ant, suc))
