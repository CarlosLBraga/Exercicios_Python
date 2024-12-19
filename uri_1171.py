lista_n = []
lista_unitario = []
lista_ordenada = []

n = int(input('digite o número de entradas: '))

#gera a entrada e adiciona na lista
for i in range(n):
    entrada = int(input(f'digite a entrada {i}: '))
    #pega valores unicos
    if entrada not in lista_unitario:
        lista_unitario.append(entrada)
    #adiciona na lista normalmente
    lista_n.append(entrada)

print(lista_n)
print(lista_unitario)

    #ordena a lista
for i in range (len(lista_unitario)):
    menor = lista_unitario[0]
    for j in range (len(lista_unitario)):
        if lista_unitario[j] < menor:
                menor = lista_unitario[j]

    lista_ordenada.append(menor)
    lista_unitario.remove(menor)

print (lista_ordenada)

for i in range (len(lista_ordenada)):
    soma = 0
    for j in range (len(lista_n)):
        if lista_ordenada[i] == lista_n [j]:
            soma += 1

    print(f'{lista_ordenada[i]} repetiu {soma}')