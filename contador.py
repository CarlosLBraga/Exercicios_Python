#esse programa faz uma contagem usando inicio, fim e passos da contagem 

from time import sleep



def contador (i, f, p):
    print ('=-' * 20)
    print(f'contagem de {i} até {f} de {p} em {p}')
    sleep(0.5)

    if p < 0:
        p *= -1

    if p == 0:
        p = 1

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM !')

    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM !')



#programa principal
contador (0, 100, 10)
print('-=' * 20)
print('AGORA É A SUA VEZ DE PERSONALIZAR A CONTAGEM !')
ini = float(input('Início: '))
fin = float(input('Fim: '))
pa = float(input('Passo: '))

contador(ini, fin, pa)