# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento.
# O seu programa deverá também mostrar o tempo que falta ou que passou do prazo

print("Seja bem-vindo ao informador de Alistamento militar!")
idade = int(input("Diga sua idade: "))
if idade < 17:
    print("Você ainda irá se alistar!")
    rest = 18 - idade
    print("Faltam {} anos para você se alistar.".format(rest))
elif idade == 18:
    print("Está na hora de você se alistar!")
elif idade > 18:
    print("Já passou do seu tempo do alistamento!")
    pas = idade - 18
    print("Já se passaram {} anos do seu alistamento, vá imediatamente se alistar!".format(pas))
# OK!