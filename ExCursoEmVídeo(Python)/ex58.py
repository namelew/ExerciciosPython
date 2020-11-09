from random import randint
from time import sleep
print('\033[1;34m-\033[m'*20, "\033[1;35mJogo da Advinhação\033[m", '\033[1;34m-\033[m'*20)
print('\033[1;34m-=-\033[m'*20)
print("\033[1;35mVou pensar em um número entre 0 e 10, tente advinhar\033[m")
print('\033[1;34m-=-\033[m'*20)
n = randint(0, 10)
print("\033[1;33mProcessando...\033[m")
sleep(2)
v = int(input("\033[1;35mEm qual número pensei?\033[m "))
t = 1
while v != n:
    t += 1
    print("\033[1;33mProcessando...\033[m")
    sleep(2)
    print("\033[1;31mErrouu!!\033[m")
    if v > n:
        print("\033[1;31mTente um número menor!\033[m")
    if v < n:
        print("\033[1;31mTente um número maior!\033[m")
    print("\033[1;34mVamos de novo!\033[m")
    v = int(input("\033[1;35mEm qual número pensei?\033[m "))
print("\033[1;33mProcessando...\033[m")
sleep(2)
print("\033[1;34mParabéns, você conseguiu me vencer.", end='')
if t <= 3:
    print(f" E em apenas {t} tentativas. Muito bem.")
else:
    print(f"\033[1;31m Mas precisou de {t} tentativas. Mais sorte na próxima.")
