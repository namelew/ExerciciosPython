print("-=-"*20)
print(" " * 11, "Detector de Palíndromos")
print("-=-"*20)
f = input("Digite uma frase: ").upper().strip().split()
j = ''.join(f)
i = ''
#Ou i = j[::-1]
#Essa estrutura substitúi o for
for l in range(len(j)-1, -1, -1):
    i += j[l]
if i == j:
    print("É um palíndromo")
else:
    print("Não é palíndromo")