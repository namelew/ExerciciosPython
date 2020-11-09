c = 1
print("Gerador de Tabuádas")
while True:
    n = int(input("Digite um número inteiro(Digite valor negativo para parar): "))
    if n < 0:
        break
    print(f"Tabuada de {n}:")
    print("-"*30)
    while c <= 10:
        print(f"{n} x {c} = {n*c}")
        c += 1
    print("-" * 30)
    c = 0
print("\033[1;31mPrograma Encerrado!")
