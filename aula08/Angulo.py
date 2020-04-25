#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians

ang = float(input("Digite o angulo: "))

seno = sin(radians(ang))
print ("O Seno de {} é igual a: {:.2f}".format(ang, seno))

cosseno = cos(radians(ang))
print ("O Cosseno de {} é igual a: {:.2f}".format(ang, cosseno))

tangente = tan(radians(ang))
print ("A Tangente de {} é igual a: {:.2f}".format(ang, tangente))
