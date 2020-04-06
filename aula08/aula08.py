#Para importar uma um modulo(biblioteca) inteira de bebidas: import bebidas
#Para eu importar apenas um item do modulo(biblioteca) bebidas eu dou: from bebidas import cafe
#Para eu importar apenas um item ou mais que um do modulo(biblioteca) bebidas eu dou: from bebidas import cafe, cha, agua
import math
import random
import emoji

#Metodo para fazer a raiz de um numero com math
num = int(input("Digite um número: "))
raiz = math.sqrt(num)
print("A Raiz de {} é igual a {:.2f}".format(num, raiz))

print(emoji.emojize(":smile:", use_aliases=True))

input("Deseja sortear um numero?")
#Este bloco de código o metodo randint ira sortear um numero aleatorio de 1 até 10
num = random.randint(1 , 10)
print("O numero sorteado foi {}.".format(num))
