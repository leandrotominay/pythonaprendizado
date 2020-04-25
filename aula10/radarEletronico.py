# Escreva um programa que leia a velocidade do carro
# se ele ultrapassar 80 km por hora mostre uma mensagem dizendo que ele foi multado
# se nao ultrapassar apenas mostrar a velocidade.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input("Digite aqui a velocidade do carro: "))
if velocidade > 80:
    valor = (velocidade - 80) * 7.00
    print("Você foi multado! "
          "Você estava a {} km/h numa via de limite de 80 km/h \nportanto, o valor de sua multa foi de {} reais."
          .format(velocidade, valor))
else:
    print("O carro estava a {} km/h portanto não receberá uma multa por estar abaixo do limite de 80 km/h imposto.".format(velocidade))