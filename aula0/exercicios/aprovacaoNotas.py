#Faça um programa que receba duas notas digitadas pelo usuário. Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.
soma = 0


for i in range(0, 2):
    notas = float(input("Digite as notas: "))
    soma += notas
    media = soma / 2

if media == 6 or media > 6:
    print("Você está aprovado!")
    print("A sua média foi de {} ".format(media))
else:
    print("Você está reprovado!")
    print("A sua média foi de {}".format(media))

