#algoritmo para calcular o valor de delta e a raiz quadrada

from math import sqrt

a = float(input('a: ' ))
b = float(input('a: ' ))
c = float(input('a: ' ))

d = (b ** 2) - 4 * a * c
if (d < 0 or a == 0.0):
    print("impossível calcular")
else:
    rd = sqrt(d)
    print (f'R1{(-b+rd) / (2 * a):.5f} \ R2{(-b-rd / (2 * a))}')