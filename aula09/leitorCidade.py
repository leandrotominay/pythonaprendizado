# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "São".

cid = str(input("Digite a cidade em que você nasceu: ")).strip() # Sempre colocar uma strip para este tipo de coisa
print(cid[:3].upper() == 'SÃO')

