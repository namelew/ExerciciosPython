# Questão 1
def ordena():
    lista = []
    for i in range(5):
        n = int(input())
        lista.append(n)
    lista.sort()
    return lista

recept = ordena()
print(recept)
# Questão 2
def primo(n):
    eh_primo = True
    if n <= 1:
        eh_primo = False
    else:
        for i in range(2, n):
            if n%i == 0:
                eh_primo = False
    if eh_primo:
        return True
    return False


print("Os números primos entre 1 e 1000 são: ", end='')
for i in range(1001):
    if primo(i):
        print(i, end=' ')
print()
# Questão 3
def index_string(string):
    for i in range(len(string)):
        print(f"Caracter '{string[i]}' posição {i}")

index_string("Joao")
# Questão 4
def muda_ponto(string):
    c = 0
    for i in range(len(string)):
        if string[i] == '.':
            c += 1
    novo = string.replace('.', ',', c)
    return novo

nova_str = muda_ponto("123.123.123")
print(nova_str)
# Questão 5
def nperfeito(n):
    div = []
    for i in range(1, n):
        if n % i == 0:
            div.append(i)
    if sum(div) == n:
        return 1
    return 0

n = int(input())
if nperfeito(n) == 1:
    print(f"{n} é um número inteiro positivo perfeito")
else:
    print(f"{n} não é um número inteiro positivo perfeito")
