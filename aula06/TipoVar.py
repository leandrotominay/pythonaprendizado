#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possiveis sobre ela
print("Exercicio 2")
thing = input('Digite algo')
print("O tipo primitivo desta variavel é: ", type(thing))
print("contém números? ", thing.isnumeric())
print("contém letras? ", thing.isalpha())
print("Está em minusculo? ", thing.islower())
print("Está em maiusculo? ",thing.isupper())

