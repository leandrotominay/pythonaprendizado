# Desenvolva um programa que leia o primeiro termo e a razão da progressão aritmética. No final, mostre os 10 primeiros
# termos dessa progressão.
termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo + razao, razao):
    print(c, end=" -> ")
