from math import hypot
co = float(input('Digite o comprimento do cateto oposto\n'))
ca = float(input('Agora, digite, do cateto adjacente\n'))
print(f'A hipotenusa do triângulo possui {hypot(co, ca):.2f}')
