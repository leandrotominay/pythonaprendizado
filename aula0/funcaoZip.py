# zip

lista1 = [1,2,3,4]
lista2 = ['Leandro','Lucas','Marcelo','Rodrigo']
lista3 = ['R$ 5,00','R$ 3,54','R$ 4,37','R$ 3,99']

for numero, nome, valor in zip(lista1, lista2, lista3):
    print(numero, nome, valor)
