# Crie um programa que leia uma frase qualquer e diga se ela é ou não um palindromo,
# desconsiderando os espaços.
# EX: APOS A SOPA -> APOS A SOPA
# EX: A SACADA DA CASA -> A SACADA DA CASA
# EX: O LOBO AMA O BOLO -> O LOBO AMA O BOLO
frase = input("Qual a frase? ").upper().replace(" ", "")
if frase == frase[::-1]:
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")