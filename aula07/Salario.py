import math

#Faça um algoritmo que leia o salário de um funconário e mostre seu novo salário com 15% de aumento.

nome = input("Bem-vindo ao sistema de visualizador de salário, digite o seu nome: ")

salario = float(input("Olá {}, Digite o seu salário em reais: ".format(nome)))
aumento = salario * 15 / 100
print("Caro {}, o seu novo salário é: {}".format(nome, aumento + salario))