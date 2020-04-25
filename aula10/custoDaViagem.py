# Desenvolva um programa que pergunte a distancia de uma viagem em km. Calcule o preço da passagem do onibus
# cobrando R$ 0,50 Por KM para viagens de até 200Km e R$0,45 para viagens longas.

print("Olá seja bem-vindo ao calculador de Custo de viagem!")
distancia = float(input("Digite a distância da viagem em Km: "))
if distancia <=200:
    preco = 0.50 * distancia
    print("O preço da sua viagem de {} km foi de R$ {:.2f}. ".format(distancia, preco))
else:
    preco = 0.45 * distancia
    print("O preço da sua viagem de {} km foi de R$ {:.2f}. ".format(distancia, preco))
