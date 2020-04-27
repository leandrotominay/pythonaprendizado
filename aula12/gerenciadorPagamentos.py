# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
# pagamento
# À vista dinheiro ou cheque: 10% de desconto.
# À vista no cartão: 5% de desconto.
# em até 2x no cartão: preço normal.
# 3x ou mais no cartão: 20% de juros.

print("Seja bem-vindo à Loja \033[1;35mRoxnay!\033[m")
preco = float(input("Digite o preço das compras: \033[1;32mR$"))
print("\033[1;32mFORMAS DE PAGAMENTO\033[m")
print("[1] à vista dinheiro/cheque.")
print("[2] à vista no cartão.")
print("[3] 2x no cartão.")
print("[4] 3x ou mais no cartão.")
opcao = int(input("Digite a opção: "))
if opcao == 1:
    precoFinal = preco - (preco * 0.10)
    print("Sua compra de R$ {} irá custar {}".format(preco, precoFinal))
elif opcao == 2:
    precoFinal = preco - (preco * 0.05)
    print("Sua compra de R$ {} irá custar {}".format(preco, precoFinal))
elif opcao == 3:
    precoFinal = preco
    print("Sua compra de R$ {} irá custar {}".format(preco, precoFinal))
elif opcao == 4:
    precoFinal = preco + (preco * 0.20)
    print("Sua compra de R$ {} irá custar {}".format(preco, precoFinal))

# OK



