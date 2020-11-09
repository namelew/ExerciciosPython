from random import randint
n = (randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50))
print(f"Os números gerados foram {n}.", end='')
print(f" O menor número foi {min(n)} e o maior foi {max(n)}")
