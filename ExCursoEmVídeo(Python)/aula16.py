lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
# tuplas são imutáveis:
#   Não pode ser executado: lanche[1] = 'Refrigerante'
# *Sem dar a posição:
# for c in lanche:
#     print(f"Eu vou comer {c}")
# *Dando a posição usando len():
# for cont in range(0, len(lanche)):
#     print(f'Eu vou comer {lanche[cont]} na posição {cont}')
# *Dando a posição utilizando enumerate():
#for p, c in enumerate(lanche):
    # print(f'Eu vou comer {c} na posição {p}')
# print("Comi para caramba!")
#sorted() organiza
print(sorted(lanche))
print(lanche)
#somando tuplas
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
#b + a != a + b
#y.count(x) = conta o número de ocorrências de x
#y.index(x) = mostra a posição da primeira ocorrencia de o x
#y.index(x, z) = busca posição de x a partir de z
print(c)
print(c.index(2, 3))
#tuplas aceitam dados de tipos diferentes
pessoa = ('Diogo', 18, 'M', 60.5)
#del(x) transforma x em um valor nulo
#tuplas são imutáveis mas podem ser apagadas
#Mas del(pessoa[0]) é um comando inválido
# del(pessoa)
print(pessoa)
