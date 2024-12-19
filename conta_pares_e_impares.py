#algoritmo para contar quantos valores pares e impares foram digtados
n = 1
par = impar = 0
while n != 0: #o programa para se digitar 0
    n = float(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print ('Você digitou {} números pares e {} números impares. '.format(par, impar))