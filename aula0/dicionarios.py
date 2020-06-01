# Listas de associação composta por uma chave e um valor correspondente
# dicionario = {'Chave':'valor'}

games = {'LoL':'League of Legends','Wow':'World of Warcraft'}
print(games['LoL'])

nomes = {"A":"Ana","B":"Bruna", "C":"Carlos"}
print(nomes['C'])

# Para navegar em cada item

for chave in nomes:
    print(chave+":"+nomes[chave])
print("\n")

#

# Para retornar as chaves e os valores da lista:
for i in games.items():
    print(i)
# Para retornar apenas as chaves:
for i in games.keys():
    print(i)

# Para retornar apenas os valores:

for i in games.values():
    print(i)