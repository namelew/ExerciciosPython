#ler 3 números e dizer qual o maior e qual o menor
import math
n1 = int(input("Digite o primeiro número\n"))
n2 = int(input("Digite o segundo número\n"))
n3 = int(input("Digite o terceiro número\n"))
#maneira clássica
#if n1 < n2 and n1 < n3:
    #print(f"{n1} é o menor valor")
#if n2 < n1 and n2 < n3:
 #   print(f"{n2} é o menor valor")
#if n3 < n1 and n3 < n2:
 #   print(f"{n3} é o menor valor")
#if n1 > n2 and n1 > n3:
 #   print(f"E {n1} é o maior valor")
#if n2 > n1 and n2 > n3:
 #   print(f"E {n2} é o maior valor")
#f n3 > n1 and n3 > n2:
#    print(f"E {n3} é o maior valor")
menor = n1
#verificando o menor
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 <n2:
    menor = n3
#verificando o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 >n2:
    maior = n3
print(f"O menor valor foi {menor}")
print(f"E o maior número foi {maior}")
