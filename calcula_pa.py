#calcula os termos de uma pa

print('10 Termos de uma PA')
n1 = int(input('digite o primeiro termo: '))
r = int(input('digite a razão: '))
decimotermo = n1 + (10 - 1) * r
for c in range (n1, decimotermo + 1, r):
    print(f'{c}', end=' > ')
print('ACABOU')