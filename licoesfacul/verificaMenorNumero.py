#Dados dois números diferentes escrever o menor na tela.

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

if (num1>num2):
    print("O número {} é o menor número!".format(num2))
else:
    print("O número {} é o menor número!".format(num1))