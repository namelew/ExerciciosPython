print("Digite 2 números e escolha o que deseja fazer com eles.")
n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
o = 0
while o != 5:
    print('''    Somar [1]
    Multiplicar [2]
    Maior [3]
    Novos Números [4]
    Sair do Programa [5]''')
    o = int(input("Opção: "))
    if o == 1:
        print(n1 + n2)
    if o == 2:
        print(n1 * n2)
    if o == 3:
        if n2 > n1:
            t = n2
            n1 = n2
            n2 = t
        print(n1)
    if o == 4:
        n1 = float(input("Número 1: "))
        n2 = float(input("Número 2: "))
