#Ex 28
#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
#qual número foi escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
print('-'*20, "Jogo da Advinhação", '-'*20)
print('-=-'*20)
print("Vou pensar em um número entre 0 e 5, tente advinhar")
print('-=-'*20)
n = randint(0, 5)
v = int(input("Em qual número pensei?\n"))
print("Processando...")
sleep(2)
if v == n:
    print("Parabens, você conseguiu me vencer.")
else:
    print(f"Que pena, ganhei. Eu pensei no número {n} e não no {v}.")
