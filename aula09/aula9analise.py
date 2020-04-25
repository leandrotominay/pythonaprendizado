#Analisar a string

frase = "Olá, o meu nome é leandro"


#frase = "Olá, o meu nome é leandro"
print(len(frase)) #len é utilizada para mostrar o comprimento de caracters de uma frase
print(len(frase.strip())) #faz a contagem junto com o metodo strip


#frase = "Olá, o meu nome é leandro"
print(frase.count('o')) #count é pra contar quantas vezes aparece o caracter especificado entre aspas



#frase = "Olá, o meu nome é leandro"
print(frase.count('o' ,0 ,13)) #Conta quantas vezes aparece o caracter especificado
# entre aspas e fazer o fatiamento



#frase = "Olá, o meu nome é leandro"
print(frase.find('leandro')) #ver quantas vezes o programa encontra a frase entre aspas na frase
# e exibe a partir de qual caracter começa a frase



#frase = "Olá, o meu nome é leandro"
print('leandro' in frase) # exibe na tela se existe ou não a palavra entre aspas na frase.


