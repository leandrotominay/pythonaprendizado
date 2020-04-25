n = input("Insira o valor de N")
if n > 0:
    n = n ** 2
else:
    if n==0:
        n = n + 1
    else:
        n = n * -1
input("O Valor de n é ", n  )