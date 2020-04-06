#Faça um programa que leia o cateto oposto, cateto adjacente e nos devolva o valor da hipotenusa usando o modulo math

import math
#h2 = ca2 + co2
#50 = 25 + 25
oposto = float(input("Digite o comprimento do cateto oposto: "))
adjacente = float(input("Digite o comprimento do cateto adjacente: "))
hipotenusa = math.hypot(oposto, adjacente)
print("A hipotenusa vai medir {2.f}".format(hipotenusa))
