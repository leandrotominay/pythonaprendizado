#Tuplas são imutaveis
campeoes = 'Darius', 'Yasuo', 'Tryndamere', 'Ornn', 'Volibear'
print(campeoes[1])
# Como escrever na tela sem colchete e aspas em questão de melhor visual
for champs in campeoes:
    print(f'Os campeões de LoL são: {champs} ')
print("Muitos campeões!")

# Para apagar uma tupla
pessoas = 'Leandro', 'Marcelo', 'Rodrigo', 'Gabriela'
del(pessoas)

try:
    print(pessoas)
except:
    print("Não existe uma tupla!")