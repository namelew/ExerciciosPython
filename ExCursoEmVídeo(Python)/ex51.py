print("-=-"*20)
print(" " * 13, "Gerador de PA")
print("-=-"*20)
p = int(input("Digite o primeiro termo: "))
r = int(input("Insira a razão: "))
s = p + (10-1)*r
for c in range(p, s + r, r):
    print(f"{c}", end='-> ')
print("FIM")