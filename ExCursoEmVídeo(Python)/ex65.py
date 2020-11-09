o = "S"
s = m = mn = 0
c = 1
while o in "Ss":
    n = int(input("Digite um número inteiro: "))
    o = str(input("Deseja continuar?[1:Sim/2:Não] ")).upper().strip()[0]
    s += n
    if c == 1:
        m = n
        mn = n
    else:
        if n > m:
            m = n
        if n < mn:
            mn = n
    c += 1
print(f"O maior e o menor número foram {m} e {mn} ", end='')
print(f"e a média dos {c} números digitados é {s/c}")
