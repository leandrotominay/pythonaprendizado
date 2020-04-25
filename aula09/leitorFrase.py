# Faça um programa que leia uma frase pelo teclado e mostre:
# 1. Quantas vezes a letra "a" aparece
# 2. Em que posição ela aparece pela primeira vez
# 3. Em que posição ela aparece a última vez.

frase = str(input("Digite uma frase: ")).strip().upper()

print("A letra A aparece {} vezes na frase.".format(frase.count('A')))
print("A primeira letra A apareceu na posição {}".format(frase.find("A")+1))
print("A ultima letra A apareceu na posição {}".format(frase.rfind("A")+1 - frase.count(" ")))