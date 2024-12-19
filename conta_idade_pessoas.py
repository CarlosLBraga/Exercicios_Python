# esse algoritmo pergunta a idade, sexo e faz a contagem
t = th = tf20 = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        t += 1
    if sexo == 'M':
        th += 1
    if sexo == 'F' and idade < 20:
        tf20 += 1

    resp = '  '
    while resp not in 'SN':
        resp = str(input('Deseja continuar ? [S/N]')).strip().upper()[0] #tratamento de string
    if resp == 'N': #termina execução se a resposta for N
        break
print(f'Total de pessoas com mais de 18 anos {t}')
print(f'ao todo temos {th} homens cadastrados')
print(f'E temos {tf20} mulheres com menos de 20 anos')