#Funções são blocos de códigos que só serão executados quando forem chamados

# OBS: def's devem ser declaradas no começo do código para o funcionamento dos outros que chamarem o mesmo!
def soma(x, y):
    print(x ,"+" ,end=" ")
    print(y, end=" = ")
    return x + y

s = soma(2, 3)
print(s)

def multiplicacao(x, y):
    return x*y

m = multiplicacao(3, 4)
print(m)