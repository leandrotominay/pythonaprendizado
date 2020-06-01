#Faça um programa que leia um número qualquer e mostre o seu fatorial
# Ex: 5! = 5x4x3x2x1 = 120
#from math import factorial
#f = factorial(n)
n = int(input("Digite um valor: "))
c = n
f = 1
print("Calculando {}!".format(n))
while c >0:
    print('{} '.format(c), end="")
    print('x ' if c > 1 else '= ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
#print('O Fatorial de {} é {}'.format(n, f))