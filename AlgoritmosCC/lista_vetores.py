# crie um arquivo python e copiei o conteúdo da questão para ele para poder testar
# 1
a = []
b = []
en_a = input().split()
for i in en_a:
    a.append(int(i))

en_b = input().split()
for i in en_b:
    b.append(int(i))

x = int(input())
print(f"Index de {x} dentro da lista A: {a.index(x)}")
for element in b:
    if b.index(element) == a.index(x):
        correspondente = element
print(f"Elemento correspondente na lista b: {correspondente}")
# 2
a = []
b = []
soma = []
entrada = input().split()
for i in range(0, len(entrada)):
    if i < 5:
        a.append(int(entrada[i]))
    else:
        b.append(int(entrada[i]))
for n in range(0, len(a)):
    s = a[n] + b[n]
    soma.append(s)
print(f"SOMA: {soma}")
# 3
maximo = minimo = 0
entrada = input().split()
for i in range(0, len(entrada)):
    if i == 0:
        maximo = minimo = int(entrada[i])
    if int(entrada[i]) > maximo:
        maximo = int(entrada[i])
    if int(entrada[i]) < maximo:
        minimo = int(entrada[i])
print(f'Valor Máximo: {maximo}\nValor Mínimo: {minimo}')
# 4
entrada = input().split()
pos = int(input('Posição a ser deletada: '))
entrada.remove(entrada[pos])
print(f"Novo Vetor: {entrada}\nTamanho: {len(entrada)}")
# 5
duplicados = []
entrada = input().split()
for i in range(0, len(entrada)):
    item = int(entrada[i])
    cont = 0
    for e in entrada:
        if int(e) == item:
            cont += 1
    if cont >= 2 and item not in duplicados:
        duplicados.append(item)
print(f"Número de elementos duplicados: {len(duplicados)}")
print('Números: ', end='')
for n in duplicados:
    print(n, end=' ')
# 6
pares = []
impares = []
entrada = input().split()
for item in entrada:
    if int(item) % 2 == 0:
        pares.append(int(item))
    else:
        impares.append(int(item))
print("Pares: ", end='')
for n in pares:
    print(n, end=' ')
print()
print("Impares: ", end='')
for n in impares:
    print(n, end=' ')
print()