#Faça um programa que mostre na tela uma contagem regressivs para o estouro de fogos de artificio, indo de 10 até 0,
#com uma pausa de 1 segundo entre eles.
import time

for cont in range(10, 0-1, -1):
    print(cont)
    time.sleep(1)

print("Feliz ano novo!")
