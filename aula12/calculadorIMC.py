# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu
# Status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do Peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida.

print("Seja bem-vindo ao calculador de IMC")
# você multiplica sua altura por ela mesma e depois divide seu peso pelo resultado da última conta.
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso / (altura * altura)
if imc < 18.5:
    print("O Seu IMC é de {:.2f} e você está abaixo do peso.".format(imc))
elif imc > 18.5 and imc < 25:
    print("O Seu IMC é de {:.2f} e você está no peso ideal.".format(imc))
elif imc > 25 and imc < 30:
    print("O Seu IMC é de {:.2f} e você está em Sobrepeso.".format(imc))
elif imc > 30 and imc < 40:
    print("O Seu IMC é de {:.2f} e você está com Obesidade.".format(imc))
elif imc > 40:
    print("O Seu IMC é de {:.2f} e você está com Obesidade Morbida".format(imc))

# OK!