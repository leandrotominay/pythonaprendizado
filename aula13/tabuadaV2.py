#Faça a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
i = int(input("Digite o número para realizar a tabuada: "))
u = int(input("Digite o ultimo numero que será feito a multiplicação da tabuada: "))
for c in range(0, u+1):
    res =+ c
    print("{} x {} = {}".format(i, c, res*i))
1