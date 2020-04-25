# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem
# ou não formar um triangulo
# pesquisar o principio matematico para fazer.
print("Olá seja bem-vindo ao analisador de Triangulo")

r1 = float(input("Digite o valor da primeira reta do triangulo"))
r2 = float(input("Digite o valor da segunda reta do triangulo"))
r3 = float(input("Digite o valor da terceira reta do triangulo"))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("É possivel formar um triangulo!")
else:
    print("Não é possivel formar um triangulo!")




