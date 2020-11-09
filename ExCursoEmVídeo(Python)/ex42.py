#complemtento ao 35
#agora deve dizer também se o triângulo é equilátero, isósceles ou escaleno
from math import fabs
print("\033[1;34m-=-"*20)
print("\033[35mAnalisador de Triângulo")
print("\033[1;34m-=-\033[0;34m"*20)
l1 = float(input("Digite a largura da primeira reta\n"))
l2 = float(input("Digite a largura da segunda reta\n"))
l3 = float(input("Digite a largura da terceira reta\n"))
if fabs(l2 - l3) < l1 < l2+l3:
    print('Estes seguimentos de reta podem formar um triângulo')
    if l2 == l3 and l3 == l1:
        print("E as retas formam um triângulo equilátero ")
    elif l2 != l3 and l1 != l3 and l1 != l2:
        print("E as retas formam um triângulo escaleno")
    else:
        print("E as retas formam um triângulo isósceles")
else:
    print("Estes seguimentos de reta não podem formar um triângulo ")
