# Operadores Aritméticos
# + Adição
# - Subtração
# * Multiplicação
# / Divisão - Divide exibindo valores inteiros
# ** Potenciação
# // Divisão inteira - Divide sem exibir valores quebrados
# % Resto da Divisão(mod, modulo)

#Ordem de precedência
# 1 - ()
# 2 - **
# 3 - * / // %%%%%%
# 4 - + -

n1 = int(input('Digite um numero'))
n2 = int(input('Digite outro numero'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
p = n1 ** n2
di = n1 // n2
print('A soma vale {}, a multiplicação vale {}, a divisão vale {:.3f}, a potenciação vale {:.3f}, e a divisão inteira vale {}'
      .format(s, m, d, p, di))
