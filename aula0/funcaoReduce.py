# função reduce
# aplica uma função em determinada lista ex: soma, subtração, multiplicaão
from functools import reduce

def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    return x / 2

lista = [1, 3, 5, 10, 20]

soma = reduce(soma, lista)
subtracao = reduce(subtracao, lista)
multiplicacao = reduce(multiplicacao, lista)
divisao = reduce(divisao, lista)

print("A soma de todos os valores da lista é igual a {} ".format(soma))
print("A subtração de todos os valores da lista é igual a {} ".format(subtracao))
print("A multiplicação de todos os valores da lista é igual a {} ".format(multiplicacao))
print("A divisão de todos os valores da lista é igual a {} ".format(divisao))
