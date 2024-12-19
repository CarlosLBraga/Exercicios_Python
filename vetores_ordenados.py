lista_1 = []
lista_2 = []
lista_3 = []
lista_ord = []

while True:
    n_1 = int(input('Digite um valor para a primeira lista (0 para terminar): '))
    if n_1 != 0:
        lista_1.append(n_1)
        if n_1 not in lista_3:
            lista_3.append(n_1)
    else:
        break

while True:
    n_2 = int(input('digite um valor para a segunda lista (0 para terminar): '))
    if n_2 != 0:
        lista_2.append(n_2)
        if n_2 not in lista_3:
            lista_3.append(n_2)
    else:
        break
print('vetor 1')
print(lista_1)
print('vetor 2')
print(lista_2)
print('vetor 3')
print(lista_3)

for i in range (len(lista_3)):
    menor = lista_3[0]

    for j in range (len(lista_3)):
        if menor > lista_3[j]:
            menor = lista_3[j]

    lista_ord.append(menor)
    lista_3.remove(menor)



print('vetor 3 ordenado')
print(lista_ord)