#jokempô
# fazer o computador jogar pedra, papel, tesoura com o usuário
#usando choice
#from random import choice
#print("\033[1;31m-=-\033[0m"*20)
#print(" "*25, "\033[1;34mJOKEMPÔ")
#print("\033[1;31m-=-\033[0m"*20)
#r = input("Vamos jogar Jokempô? Sim ou não?\n")
#if r == "Sim":
#    lista = ["Pedra", "Papel", "Tesoura"]
#    o = input("Pedra, Papel ou Tesoura?\n")
#    c = choice(lista)
   # print(c)
  #  if c == "Pedra" and o == "Tesoura":
 #       print("Uma pena! Eu ganhei, mais sorte na próxima.")
#    elif c == "Tesoura" and o == "Papel":
    #    print("Uma pena! Eu ganhei, mais sorte na próxima.")
   # elif c == "Papel" and o == "Pedra":
#        print(c)
#        print("Uma pena! Eu ganhei, mais sorte na próxima.")
  #  elif c == "Pedra" and o == "Papel":
 #       print("Parabéns! Você me ganhou!")
#    elif c == "Papel" and o == "Tesoura":
     #   print("Parabéns! Você me ganhou!")
    #elif c == "Tesoura" and o == "Pedra":
    #    print("Parabéns! Você me ganhou!")
    #elif c == o:
   #     print("Parece que empatamos!")
  #  else:
 #       print("Coloque uma opção válida!")
#elif r == "Não":
 #   print("Uma pena! Fica para a próxima")
#else:
    #print("Erro! Dê uma resposta válida")
#usando radint
from random import randint
from time import sleep
i = ["Pedra", "Papel", "Tesoura"]
c = randint(0, 2)
print("[0]Pedra\n[1]Papel\n[2]Tesoura")
j = int(input("Qual a sua jogada?\n"))
print("Jo")
sleep(0.5)
print("Ken")
sleep(0.5)
print("Pô")
sleep(0.5)
print("-=-"*11)
sleep(0.5)
print(f"Computador jogou {i[c]}")
sleep(0.5)
print(f"Usuário jogou {i[j]}")
sleep(0.5)
print("-=-"*11)
sleep(0.5)
if c == j:
    print("Parece que empatamos")
elif c == 0 and j == 2:
    print("Uma pena! Eu ganhei, mais sorte na próxima.")
elif c == 1 and j == 0:
    print("Uma pena! Eu ganhei, mais sorte na próxima.")
elif c == 2 and j == 1:
    print("Uma pena! Eu ganhei, mais sorte na próxima.")
elif c == 2 and j == 0:
    print("Parabéns! Você me ganhou!")
elif c == 0 and j == 1:
    print("Parabéns! Você me ganhou!")
elif c == 1 and j == 2:
    print("Parabéns! Você me ganhou!")