# Faça um programa que leia um número inteiro, e diga se ele é ou não um numero primo
# numero primo é apenas divisivel por 1 e por ele mesmo.

num = int(input("Digite um numero: "))
if num % 1 == 0 and num % num == 0:
    print("O número {} é um numero primo!".format(num))
else:
    print("O número {} não é um numero primo!".format(num))