#Desenvolva um programa que leia seis numéros inteiros e mostre a soma apenas daqueles que forem pares
#se for impar, desconsidere-o
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input("Digite o {} valor: ".format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print("Você informou {} valores pares e o resultado da soma é igual a {}".format(cont, soma))