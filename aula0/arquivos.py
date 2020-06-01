textocompleto = open("test.txt")
print("\n", textocompleto.read())

textoemlinhas = open("test.txt")
linhas = textoemlinhas.readlines()
print("\n", linhas)


textoemlinha = open("test.txt")
print("\n", textoemlinha.readline())

#read() - Lê o arquivo inteiro
#readline() - Lê apenas uma linha
#readlines() - Lê arquivo e o armazena em uma lista