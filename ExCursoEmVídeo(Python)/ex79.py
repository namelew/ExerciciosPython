from time import sleep
l = list()
r = ' '
v = 0
while r not in "Nn":
    v = l[:]
    n = int(input("Digite um valor: "))
    l. append(n)
    while n in v:
        print("Valor duplicado! Tente novamente!")
        l.pop()
        n = int(input("Digite um valor: "))
        l.append(n)
    print("Adicionando valor...")
    sleep(1)
    r = str(input("Deseja continuar?[S/N] ")).upper()[0]
    while r not in "SsNn":
        r = str(input("Deseja continuar?[S/N] ")).upper()[0]
print(l.sort())
