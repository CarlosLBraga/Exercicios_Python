#uri 1040 esse algoritmo calcula a média do aluno e verifica se foi aprovado

def media (n1, n2, n3, n4):
    med = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / (10)
    return med

def exame (med, exam):
    ex = (med + exam) / 2
    return ex


n1 = float(input('a'))
n2 = float(input('b'))
n3 = float(input('c'))
n4 = float(input('d'))

med = media(n1, n2, n3, n4)
print(f'Media: {med:.1f}')

if med >= 7.0:
    print('Aluno provado.')
elif med < 5.0:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    exam = float(input('exame: '))

    print(f'nota do exame: {exam:.1f}')
    ex = exame(med, exam)
    if ex >= 5:
        print('Aluno aprovado.')
        print(f'Media final {ex:.1f}')
    else:
        print('Aluno reprovado.')
        print(f'Media final: {ex:.1f}')