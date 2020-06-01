#Como criar e escrever em um arquivo:

w = open("arquivo2.txt", "w")
w.write("Este é o meu arquivo!")
w.close()

#Como abrir e ver o que eu escrevi nele:

textocompleto = open("arquivo2.txt")
print(textocompleto.read())