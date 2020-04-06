import math

#Faça um algortimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
#5%
produto = float(input("Digite o seu preço: "))
desconto = produto * 5 / 100
print("O preço promocional ficará: {} ".format( desconto - produto))
