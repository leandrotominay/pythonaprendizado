# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final de acordo com a
# sua média atingida:
#
# Média abaixo de 5.0: REPROVADO.
# Média entre 5.0 e 6.9: RECUPERAÇÃO.
# Média 7.0 ou superior: APROVADO.
print("Seja bem-vindo ao calculador de média do aluno!")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media <= 5.0:
    print("REPROVADO.")
    print("A média do aluno foi de {:.1f}".format(media))
if media > 5.0 and media < 7:
    print("RECUPERAÇÃO.")
    print("A média do aluno foi de {:.1f}".format(media))
if media >= 7.0:
    print("APROVADO.")
    print("A média do aluno foi de {:.1f}".format(media))

# OK