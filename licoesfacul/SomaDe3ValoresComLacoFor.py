# Crie um programa em Python que calcule a soma de 3 números
soma = 0
for i in range(0, 3):
    numero = int(input('Digite um valor: '))
    soma += numero
print('Soma dos valores: {}'.format(soma))