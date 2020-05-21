#Crie um programa que mostre na tela todos os numéros pares que estão no intervalo entre 1 e 50.

i = int(input("Digite o primeiro numero da contagem: "))
u = int(input("Digite o ultimo numero da contagem: "))
for c in range(i, u+1):
    if c % 2 == 0:
     print(c, end=" ")