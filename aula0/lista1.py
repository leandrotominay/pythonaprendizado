# Para criar listas:
minha_lista = ["Yasuo", "Zed", "Masteryi"]
minha_lista2 = [1,2,3,4,5]

# Para exibir itens da lista:
print(minha_lista[0], end=" ")
print(minha_lista[1], end=" ")
print(minha_lista[2])

# Para adicionar itens na lista

campeoes = ["Rammus", "Sejuani", "Nocturne"]
campeoes.append("Nunu")
print(campeoes)

# Verificando se existe um item na minha lista

pogchamp = ["Yasuo", "Darius", "Tryndamere", "Soraka"]

if "Soraka" in pogchamp:
    print("O campeão verificado está nesta lista!")
else:
    print("O campeão verificado não está na lista!")

# Removendo elementos de uma lista

melhoreschamps = ["Yasuo", "Gnar", "Soraka", "Udyr", "Sona"]

del melhoreschamps [3:5]
print(melhoreschamps)