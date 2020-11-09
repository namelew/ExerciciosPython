from random import randint
print("-=-"*20)
print("Vamos Jogar Par ou Ímpar?")
print("-=-"*20)
comp = randint(1, 10)
v = 0
while True:
    j = int(input("Diga um valor: "))
    o = str(input("Par ou Impar? [P/I] ")).upper().strip()[0]
    while o not in "PpIi":
        o = str(input("Par ou Impar? [P/I] ")).upper().strip()[0]
    t = comp + j
    print("-" * 60)
    print(f"Jogador jogou {j} e o computador, {comp}. O total deu {t}")
    print("-" * 60)
    if o in "Pp" and t % 2 == 0:
        print("Você Venceu!")
        print("Vamos jogar de novo?")
        v += 1
        comp = randint(1, 10)
        print("-=-"*20)
    elif o in "Ii" and t % 2 != 0:
        print("Você Venceu!")
        print("Vamos jogar de novo?")
        v += 1
        comp = randint(1, 10)
        print("-=-" * 20)
    else:
        print("Você Perdeu!", end='')
        break
print(f"O jogador conseguiu um total de {v} vitórias. Obrigado por Jogar!")