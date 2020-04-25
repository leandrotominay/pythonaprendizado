# Escreva um programa que pergunte o salario de um funcionario
# e calcule o valor do seu aumento
# Para salarios superiores a R$ 1.250,00 calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%.

print("Olá seja bem-vindo ao calculo de aumento.")
salario = float(input("Digite o seu salário: "))
if salario > 1.250:
    aumento = (salario * 0.10) + salario
    print("O seu salário é: {:.3f}".format(aumento))
else:
    aumento = (salario * 0.15) + salario
    print("O seu salário é: {:.3f}".format(aumento))
