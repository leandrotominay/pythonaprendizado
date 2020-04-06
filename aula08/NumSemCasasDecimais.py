#Crie um programa que leia um número qualquer pelo teclado e mostre na tela a sua porção inteira
import math

num = float(input("Digite um número: "))
print("O Numero {} sem casas decimais e arredondado fica: {} ".format(num, math.trunc(num)))