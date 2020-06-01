# Crie um programa que leia dois valores e mostre um menu na tela
#
# [1] SOMAR
# [2] SUBTRAIR
# [3] MULTIPLICAR
# [4] MAIOR NUMERO
# [5] NOVOS NÚMEROS
# [6] SAIR DO PROGRAMA
n1 = int(input('Digite o 1º numero: '))
n2 = int(input('Digite o 2º numero: '))
opcao = 0
while opcao != 6:
    opcao = int(input("[1] SOMAR\n[2] SUBTRAIR\n[3] MULTIPLICAR\n[4] MAIOR NUMERO\n[5] NOVOS NUMEROS\n[6] SAIR DO PROGRAMA\nQual opção deseja? "))
    if opcao == 1:
        numeros = n1 + n2
        print(numeros)
    elif opcao == 2:
        numeros = n1 - n2
        print(numeros)
    elif opcao == 3:
        numeros = n1 * n2
        print(numeros)
    elif opcao == 4:
        if n1 > n2:
            print("O maior numero é o {}".format(n1))
        else:
            print("O maior numero é o {}".format(n2))
    elif opcao == 5:
        n1 = int(input('Digite o 1º numero: '))
        n2 = int(input('Digite o 2º numero: '))
    elif opcao == 6:
        print("FIM")
    else:
     print("Opção inválida.")

