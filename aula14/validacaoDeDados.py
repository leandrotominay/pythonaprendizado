#Faça um programa que leia o sexo de uma pessoa, mas só aceite 'M' ou 'F', caso esteja errado peça a digitação novamente
# até obter um valor correto
sexo = 0

sexo = str(input("Digite o seu sexo [M/F]: ")).strip().upper()[0]
while sexo not in 'MmFf':
    print("Gênero invalido, digite novamente.")
    sexo = str(input("Digite o seu sexo [M/F]: ")).upper()

