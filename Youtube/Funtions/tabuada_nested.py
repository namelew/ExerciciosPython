# Exercício
# Tabuadas até o valor n
def tabu():
    multiplos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    def tabuada(n):
        for c in range(n):
            print(f"Tabuada de {c+1}")
            for mut in multiplos:
                print(f"{c+1} x {mut} = {(c+1) * mut}")
    return tabuada

objeto = tabu()
valor = int(input("Valor Inteiro: "))
objeto(valor)
