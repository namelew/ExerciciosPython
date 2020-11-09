print("Sequência de Fibonacci:")
print("Digite a quantidade de termos que deseja ver.")
n = int(input("Quantidade de termos: "))
c = 3
t1 = 0
t2 = 1
print(t1, end='-> ')
print(t2, end='-> ')
while c <= n:
    t3 = t1 + t2
    print(t3, end='-> ')
    t1 = t2
    t2 = t3
    c += 1
print("FIM")
