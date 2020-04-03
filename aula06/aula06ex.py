# Crie um programa que leia dois numeros depois mostre a soma entre eles.
print("Exercicio 1")
number1 = int(input("Digite o primeiro número a ser somado"))
number2 = int(input("Digite o segundo número a ser somado"))
soma =  number1 + number2
print("A soma de {} e {} é igual a {}".format(number1, number2, soma))

#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possiveis sobre ela
print("Exercicio 2")
thing = input('Digite algo')
print("O tipo primitivo desta variavel é: ", type(thing))
print("contém números? ", thing.isnumeric())
print("contém letras? ", thing.isalpha())
print("Está em minusculo? ", thing.islower())
print("Está em maiusculo? ",thing.isupper())

