# Função map
# pega cada elemento da lista e aplica a uma determinada função

def dobro(x):
    return x*2

valor = [1, 2, 3, 4, 5, 6]
dobrado = map(dobro, valor)
dobrado = list(dobrado)
print(dobrado)