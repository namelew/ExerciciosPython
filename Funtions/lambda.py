# lambdas são funções simplificadas que precisam de variáveis onde podem ser armazenadas
def soma(x,y,z):
    return x+y+z
print(soma(1, 2, 3))
s = (lambda x,y,z: x+y+z) # equivalente a função soma
print(s(1, 2, 3))