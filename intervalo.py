#algoritmo para encontra em qual intervalo está o valor n

n = float(input('m '))

if 0 <= n <= 25:
    print('intervalo [0,25]')
elif 25 <= n <= 50:
    print('intervalo [25,50]')
elif 50 <= n <= 75:
    print('intervalo [50,75]')
elif 75 <= n <= 100:
    print('intervalo [75,100]')
else:
    print('fora do intervalo')