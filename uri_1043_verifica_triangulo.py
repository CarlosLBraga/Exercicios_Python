#uri 1043 verifica se é possível formal um triangulo
from time import sleep
a = float(input('digite a '))
b = float(input('digite b '))
c = float(input('digite c '))

if a + b > c and a + c > b and c + b > a:
    p = a + b + c
    sleep(0.2)
    print(f'é posível formar um triângulo e o seu perímetro é {p}')
else:
        print('Não foi possível formar um triângulo :( ')
        sleep(0.3)
        print('Mas podemos formar um trapézio e calcular sua área ...')
        sleep(0.3)
        res = str(input('Gostaria de testar ? sim (s) ou não (n)')).strip().upper()
        if res in 'Ss':
            area = ((a + b) * c) / 2
            sleep(0.3)
            print(f'Formamos um trapézio e sua área é {area} :D ')
        else:
            sleep(0.4)
            print('.-.')
print('Volte Sempre')