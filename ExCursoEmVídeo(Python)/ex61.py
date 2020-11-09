print("-=-"*20)
print(" " * 13, "Gerador de PA")
print("-=-"*20)
p = int(input("Digite o primeiro termo: "))
r = int(input("Insira a razão: "))
t = p
c = 1
while c <= 10:
    print(f"{t}", end='-> ')
    t += r
    c += 1
print("FIM")
