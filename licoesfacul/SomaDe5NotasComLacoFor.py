# Crie um programa em Python que calcule a soma de 5 notas
#
soma = 0
for cont in range(0, 5):
    nota = int(input('Digite uma nota: '))
    soma += nota
print('Soma das notas: {}'.format(soma))

