lista1 = [1, 2, 3, 4, 5]
print(lista1,end=", ")
# list comprehension = list = [valor, laço, condição]
lista2 = [i**2 for i in lista1]
print(lista2,end=", ")

# imprimir apenas pares
lista3 = [i for i in lista1 if i%2==0]
print(lista3,end=", ")

#imprimir apenas impares
lista3 = [i for i in lista1 if i%2==1]
print(lista3,end=" ")