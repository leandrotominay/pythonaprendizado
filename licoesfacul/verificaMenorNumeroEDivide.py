#Dados dois números diferentes dividir o maior pelo menor valor.

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

if(num1>num2):
    divisao = num1/num2
    print("O Resultado da divisão de {} por {} é igual a: {}".format(num1, num2, divisao))
else:
    divisao = num2/num1
    print("O Resultado da divisão de {} por {} é igual a: {}".format(num2, num1, divisao))