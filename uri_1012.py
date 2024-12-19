a = float(input("digite o valor de A: "))
b = float(input("digite o valor de B: "))
c = float(input("digite o valor de C: "))

a_triangulo = (a * c) / 2
a_circulo = 3.14159 * (c ** 2)
a_trapezio = ((a + b) * c) / 2
a_quadrado = b * b
a_retangulo = a * b


print(f'TRIANGULO: {a_triangulo :0.3f}')
print(f'CIRCULO: {a_circulo :0.3f}')
print(f'TRAPEZIO: {a_trapezio:0.3f}')
print(f'QUADRADO: {a_quadrado:0.3f}')
print(f'RETANGULO: {a_retangulo:0.3f}')