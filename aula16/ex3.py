# Crie um programa que vai gerar 5 números aleatorios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor.
from random import randint
for num in range(0, 5):
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    num3 = randint(0, 100)
    num4 = randint(0, 100)
    num5 = randint(0, 100)
    lista = (num1, num2, num3, num4, num5)
print(f'A lista aleatoria gerada é : {lista}')
maior = sorted(lista, reverse=True)
menor = sorted(lista)
print(f'O maior valor é : {maior[0]}')
print(f'O menor valor é : {menor[0]}')