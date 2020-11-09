print("-=-"*20)
print(" " * 13, "Gerador de PA")
print("-=-"*20)
p = int(input("Digite o primeiro termo: "))
r = int(input("Insira a razão: "))
t = p
total = 0
c = 1
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print(f"{t}", end='-> ')
        t += r
        c += 1
    print("PAUSA")
    mais = int(input("Deseja gerar mais termos? Quantos? Digite 0 para finalizar. "))
print("FIM")