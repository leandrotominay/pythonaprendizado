import math

#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
print("**Programa que le numero inteiro e exibe seu dobro, triplo e raiz quadrada**")
number = int(input('Digite um numero: '))
dobro = number * 2
triplo = number * 3
raiz = math.sqrt(number)
print("O Dobro do numero {} é igual a {}, seu triplo {} e a sua raiz quadrada {}"
      .format(number, dobro, triplo, raiz))
