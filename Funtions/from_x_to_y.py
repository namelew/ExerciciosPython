# Exercício
# Função que retorna os valores entre x e y
def from_to(x, y):
    print(x)
    if x == y:
        return x
    return from_to(x + 1, y)


from_to(3, 6)