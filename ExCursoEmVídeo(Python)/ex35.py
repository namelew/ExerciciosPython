#ler 3 seguimentos de retas e dizer se ele pode ou não formar um triângulo
#a função fabs() retorna o valor absoluto de um valor x
from math import fabs
print("-=-"*20)
print("Analisador de Triângulo")
print("-=-"*20)
l1 = float(input("Digite a largura da primeira reta\n"))
l2 = float(input("Digite a largura da segunda reta\n"))
l3 = float(input("Digite a largura da terceira reta\n"))
if fabs(l2 - l3) < l1 < l2+l3:
    print('Estes seguimentos de reta podem formar um triângulo')
else:
    print("Estes seguimentos de reta não podem formar um triângulo ")
