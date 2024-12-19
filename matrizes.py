import random

def montar_matriz (linha, coluna):
    matriz = []
    for i in range (linha):
        linha_matriz = []
        for j in range (coluna):
            linha_matriz.append(random.randint(-10, 10))

        matriz.append(linha_matriz)

    return matriz

def imprimir_matriz (matriz):
    for i in range (len(matriz)):
        print(matriz[i])

def menu ():
    print('*' * 30)
    print('1 - Somar')
    print('2 - Multiplicar')
    print('3 - Maior Linha')
    print('4 - Média Matriz')
    print('5 - Sair')
    print('*' * 30)

def somar_matriz (matriz_1, matriz_2):
    matriz_3 = []

    for i in range (len(matriz_1)):
        linha = []
        for j in range (len(matriz_2[0])):
            soma = matriz_1[i][j] + matriz_2[i][j]
            linha.append(soma)
        matriz_3.append(linha)

    return matriz_3

def multiplicar_matriz (matriz_1, matriz_2):
    if len(matriz_1) != len(matriz_2[0]):

        return print('impossível calcular')

    else:
        matriz_3 = []
        for i in range (len(matriz_1)):
            linha = []
            for j in range (len(matriz_2[0])):
                soma = 0
                for k in range (len(matriz_2)):
                    soma += matriz_1[i][k] * matriz_2[k][j]
                linha.append(soma)
            matriz_3.append(linha)

        imprimir_matriz(matriz_3)

def maior_linha (matriz):
    maior = 0
    indice = 0
    for i in range (len(matriz)):
        aux = sum(matriz[i])
        if maior == 0:
            maior = sum(matriz[0])
            indice = 0

        else:
            if maior < aux :
                maior = aux
                indice = i
    print(f'{matriz[indice]}, {maior}')

def media_matriz (matriz):
    soma = 0

    for i in range (len(matriz)):
        for j in range (len(matriz[0])):
            soma += matriz[i][j]

    media = soma / (len(matriz) * len(matriz[0]))
    return media

n_1 = int(input('Dimensão linhas (n) da matriz A: '))
m_1 = int(input('Dimensão colunas (m) da matriz A: '))

print('Matriz A')
matriz_a = montar_matriz(n_1, m_1)
imprimir_matriz(matriz_a)

n_2 = int(input('Dimensão linhas (n) da matriz B: '))
m_2 = int(input('Dimensão colunas (m) da matriz B: '))

print('Matriz B')
matriz_b = montar_matriz(n_2, m_2)
imprimir_matriz(matriz_b)

while True:
    menu()

    opcao = int(input('digite a opção desejada: '))
    print(f'Sua opção foi {opcao}')

    if opcao == 5:

        break

    elif opcao == 1:
        print('Matriz C')

        matriz_c = somar_matriz(matriz_a, matriz_b)
        imprimir_matriz(matriz_c)


    elif opcao == 2:
        print('Matriz C')
        matriz_c = multiplicar_matriz(matriz_a, matriz_b)



    elif opcao == 3:
        print('Maior Matriz A:')
        maior_linha(matriz_a)

        print('Maior Matriz B:')
        maior_linha(matriz_b)

    elif opcao == 4:

        print('Média da matriz A')
        print(media_matriz(matriz_a))

        print('Média da matriz B')
        print(media_matriz(matriz_b))