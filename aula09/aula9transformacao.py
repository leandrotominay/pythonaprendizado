# Transformação

frase = "Olá, o meu nome é Leandro"

#frase = "Olá, o meu nome é Leandro"
print(frase.replace("Leandro", "Gabriela")) #o replace faz com que troque a primeira palavra entre aspas, pela segunda


#frase = "Olá, o meu nome é Leandro"
print(frase.upper()) #upper faz com que todos os caracteres da frase fique em maiusculo
print(frase.upper().count("O")) # todos os caracteres ficam em maiusculo e faz a contagem do caracter especificado
# entre aspas no count


#frase = "Olá, o meu nome é Leandro"
print(frase.lower()) #lower faz com que todos os caracteres da frase fique em minusculo


#frase = "Olá, o meu nome é Leandro"
print(frase.capitalize()) #pega uma string inteira, joga tudo pra minusculo e
# faz com que a primeira letra comece em maiusculo


#frase = "Olá, o meu nome é Leandro"
print(frase.title()) #onde tiver espaço ele vai fazer com que cada começo de palavra fique em maiusculo


#frase = "Olá, o meu nome é Leandro"
print(frase.strip()) #Remove todos os espaços inuteis da frase


#frase = "Olá, o meu nome é Leandro  "
print(frase.rstrip()) # Remove somente os ultimos espaços excedentes


#frase = "  Olá, o meu nome é Leandro"
print(frase.lstrip()) # Remove somente os primeiros espaços excedentes