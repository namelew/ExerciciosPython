num = [2, 5, 9, 1]
num[2] = 3
# num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
print(num)
num.pop(2)
if 5 in num:
    num.remove(5)
else:
    print("Não achei o 5")
#x.remove(z) = elimina a primeira ocorrencia de y na lista
#x.pop() = remove o último elemento
#x.pop(y) = remove o elemento y
print(num)
print(f"Essa lista tem {len(num)} elementos")
valores = list() # ou valores = []
for count in range(0, 3):
    valores.append(int(input("Digite um valor: ")))
#for v in valores:
#    print(f"{v}...", end='')
for c, v in enumerate(valores):
    print(f"Na posição {c} encontrei o valor {v}!")
print("Cheguei ao final da lista!")
# Peculiaridade do Python:
# Lista = Lista é uma ligação entre duas listas
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f"Lista A: {a}")
print(f"Lista B: {b}")
# Para fazer uma cópia é necessário Lista B = Lista A[:]