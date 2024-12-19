#algoritmos de ordenação

def bubble_sort(vetor):
    for i in range(len(vetor)):
        for j in range(i+1, len(vetor)):
            if vetor[i] > vetor[j]:
                aux = vetor[i]
                vetor[i] = vetor[j]
                vetor[j] = aux

def selection_sort(vetor):
    for i in range(len((vetor))):
        i_menor = i

        for j in range(i+1, len(vetor)):
            if vetor[j] < vetor[i_menor]:
                i_menor = j

        aux = vetor[i]
        vetor[i] = vetor[i_menor]
        vetor[i_menor] = aux

def insertion_sort(vetor):
    for i in range(1, len(vetor)):
        j = i
        temp = vetor[i]

        while j > 0 and vetor[j-1] > temp:
            vetor[j] = vetor[j-1]
            j -= 1

        vetor[j] = temp

lista = [3, 2, 4, 1, 5, 10, 9]
print(lista)
insertion_sort(lista)
print(lista)

lista = [3, 2, 4, 1, 5, 10, 9]
selection_sort(lista)
print(lista)

lista = [3, 2, 4, 1, 5, 10, 9]
bubble_sort(lista)
print(lista)