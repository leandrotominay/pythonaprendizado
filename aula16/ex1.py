# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte
# Seu programa deverá ler um numero pelo teclado (entre 0 a 20) e mostra-ló por extenso

numeros = {'1':'Um','2':'Dois','3':'Três','4':'Quatro','5':'Cinco','6':'Seis','7':'Sete','8':'Oito','9':'Nove','10':'Dez',
           '11':'Onze','12':'Doze','13':'Treze','14':'Catorze','15':'Quinze','16':'Dezesseis','17':'Dezessete','18':'Dezoito',
           '19':'Dezenove','20':'Vinte'}
num = 0
while num > 0 or num < 20:
   num = int(input("Digite um numéro de 1 até 20 e traremos o resultado por extenso: "))
   try:
    print(numeros[f'{num}'])
   except:
       print("O numero digitado não está entre 1 e 20, tente novamente.")
