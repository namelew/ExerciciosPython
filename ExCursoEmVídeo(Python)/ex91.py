from random import randint as rd
from time import sleep as slp
from operator import itemgetter
jogo = {
    'jogador 1': rd(1, 6),
    'jogador 2': rd(1, 6),
    'jogador 3': rd(1, 6),
    'jogador 4': rd(1, 6)
}
ranking = list()
print('Valores Sorteados:')
for k, v in jogo.items():
    print(f'O {k} jogou {v}')
    slp(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)#key=itemgetter(0) = ordena por key
print('-='*30)
print("PÓDIUM")
for i, v in enumerate(ranking):
    print(f"{i+1}º lugar: {v[0]} com {v[1]}")
    slp(1)
