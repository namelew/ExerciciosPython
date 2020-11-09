#comparar valores inteiros e dizer
#qual é maior ou se ambos são iguais
n1 = int(input("Insira o primeiro valor "))
n2 = int(input("Insira o segundo valor "))
if n1 > n2:
    print(f"{n1} é o maior")
elif n2 > n1:
    print(f"{n2} é o maior")
else:
    print("Ambos são iguais")