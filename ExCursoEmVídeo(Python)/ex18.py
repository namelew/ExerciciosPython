from math import sin, tan, cos, radians
angulo = int(input('Digite um ângulo, sem "º"\n'))
print(f'Sen = {sin(radians(angulo)):.3f}\nCos = {cos(radians(angulo)):.3f} \nTg = {tan(radians(angulo)):.3f}')
