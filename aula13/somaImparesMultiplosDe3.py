# Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no
# intervalo de 1 até 500.
# 1, 500+1
s = 0
for c in range(1, 500+1):
    if c % 2 != 0 and c % 3 == 0:
        print(c, end=" ")
        s += c
print(" ")
print("A soma de todos os numeros impares que são múltiplos de três é igual a : {} ".format(s))

