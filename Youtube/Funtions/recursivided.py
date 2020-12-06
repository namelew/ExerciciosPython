# função não recursiva
def soma(x, y):
    # print(soma()) gera um erro
    print(x + y)

# função recursiva
def fatorial(n):
    if n == 1:
        return n
    return fatorial(n-1) * n
# funcionamento:
# caso fatorial de 5:

# return fat(5) = fat(4) * 5 = 1 * 2 * 3 * 4 * 5  
# return fat(4) = fat(3) * 4 = 1 * 2 * 3 * 4
# return fat(3) = fat(2) * 3 = 1 * 2 * 3
# return fat(2) = fat(1) * 2 = 1 * 2
# return fat(1) = 1

# em outras palavras:
# ela decompoe o problema e depois recompoem os resultados para encontrar o resul final

soma(2, 3)
print(fatorial(5))
