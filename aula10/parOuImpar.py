# Crie um programa que leia um numero qualquer e
# mostre na tela se ele é impar ou par.

print("Seja bem-vindo ao identificador de números impares e pares")
num = int(input("Digite um número: "))
if num % 2 == 0 : # OBS: % significa o resto da divisão!
    print("O número é par!")
else:
    print("O número é impar!")

