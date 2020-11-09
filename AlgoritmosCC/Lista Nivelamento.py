#1-1
n = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
m = ((n + n2) *3 + n3 *4)/3
print(f"A média do aluno foi {m:.2f}")
#1-2
t = float(input("Tempo(h): "))
d = float(input("Distância(Km): "))
v = d/t
print(f"O objeto está em {v/1224:.2f} Mach")
#1-3
f = int(input("Ferro de Solda(unidade): "))
e = int(input("Estanho(unidade): "))
s = int(input("Sugador de Solda(unidade): "))
pf = f*34.67
if f >= 10 and f <=20:
    c = pf * 0.90 + e*14.56 + s*18.90
elif f>20:
    c = pf * 0.82 + e * 14.56 + s * 18.90
else:
    c = pf + e * 14.56 + s * 18.90
print(f"O valor da compra foi R$ {c:.2f}")

#1-4
a = int(input("A: "))
b = int(input("B: "))
c = a
a = b
b = c
print(f"A: {a}\nB: {b}")
#1-5
ta = float(input("Taxa de Alfabetização: "))
nu = int(input("N. de Universidades: "))
np = int(input("N. de Parques: "))
rp = float(input("Renda per capita: "))
if ta < 80 or rp < 1000:
    print("Não aconselhável")
elif 90 > ta >= 85 and 1200 > rp > 1000 and nu > 0:
    print("Aconselhável com Precaução")
elif ta > 90 and 1200 >= rp > 1000 and nu >= 2:
    print("Aconselhável")
else:
    print("Formente Aconselhável")
#2-1
n = int(input("Digite um valor: "))
for i in range(1, n+1):
    if i % 2 == 0:
        print(i)
#2-2
div = int(input("Dividadendo: "))
ds = int(input("Divisor: "))
while div >= ds:
    div -= ds
print("Resto:", div)

#2-3
print("Digite 0 em volume para sair")
c = ca = cr = mv = mp = 0
while True:
    v = float(input("Volume(mm³): "))
    if v == 0:
        break
    p = float(input("Peso(g): "))
    if 5.243 <= v <= 5.775 and 9.2 <= p <= 10.8:
        ca += 1
    else:
        cr += 1
    if c == 0 or v > mv:
        mv = v
    if c == 0 or p > mp:
        mp = p
    c += 1
print("-="*30)
print(f"N.Esferas Informadas: {c}\nN.Esferas Aceitas: {ca}\nN.Esferas Recusadas: {cr}")
print(f"Maior peso: {mp}\nMaior Volume: {mv}")

#2-4
print("Digite Idade: 0, para sair")
p = p70 = sp = p35 = a16 = 0
while True:
    idade = int(input("Idade(Anos): "))
    if idade == 0:
        break
    altura = float(input("Altura(Metros): "))
    peso = float(input("Peso(Kg): "))
    if peso < 70:
       p70 += 1
    if 35 <= idade <= 40:
        sp += peso
        p35 += 1
    if altura < 1.60:
        a16 += 1
    p += 1
print("Q. Pessoas - de 70 kg:", p70)
print(f"Média Pesos Pessoas entre 35-45 anos: {sp/p35:.2f} Kg")
print(f"Média de Pessoas com - de 1,60 m de altura: {a16/p*100:.2f} %")
#2-5
from random import randint as rd
from time import sleep as slp
j1 = input(f"Jogador 1: ")
j2 = input(f"Jogador 2: ")
p1 = p2 = 0
while True:
    d1 = rd(1, 6)
    d2 = rd(1, 6)
    slp(1)
    print("-=" * 10)
    slp(1)
    print(f"{j1} jogou: ", d1)
    slp(1)
    print(f"{j2} jogou: ", d2)
    slp(1)
    print("=+"*10)
    p1 += d1
    p2 += d2
    slp(1)
    print(f"{j1} possui: {p1} pontos")
    slp(1)
    print(f"{j2} possui: {p2} pontos")
    if p1 >= 27:
        slp(1)
        print(f"{j1} venceu")
        break
    if p2 >= 27:
        slp(1)
        print(f"{j2} venceu")
        break
#3-1
num = []
for i in range(0, 20):
    num.append(int(input("Digite um número: ")))
for n in num:
    print(f"O quadrado de {n} é {n**2}")
#3-2
num = []
print("Digite 0 ou um número negativo para sair.")
s = c = 0
while True:
    n = int(input("Digite um valor: "))
    if n <= 0:
        break
    num.append(n)
    s += n
    c += 1
print(f"Média dos Números: {s/c:.2f}")
print("Os números menores que a média foram: ", end='')
for i in num:
    if i < s/c:
        print(i, end=' ')
print(".")

#3-3
prod = ['Arroz 1Kg', 'Açúcar Kg', 'Pão Un', 'Leite L', 'Margarina Un', 'Óleo L', 'Café Kg']
prec = [3.8, 2.8, 0.1, 2.1, 4.8, 2.3, 6.7]
compra = 0
while True:
    cod = int(input("Código do Produto: "))
    if cod == -1:
        break
    print(f"Produto: {prod[cod]}")
    q = int(input("Quantidade: "))
    compra += prec[cod] * q
print(f"Preço Total da Compra: R$ {compra:.2f}")

#3-4
pont = []
s = 0
p = 0
for n in range(0, 150):
    p = int(input(f"Pontuação Participante {n+1}: "))
    pont.append(p)
    s += p
media = s/len(pont)
print(f"A média das notas foi {media:.2f} e", end=" ")
print("os aprovados para a próxima fase foram: ")
for i in range(0, len(pont)):
    if pont[i] > media:
        print(f"{i+1}º Participante")

#3-5
l1 = []
l2 = []
soma = []
print("Valores para a primeira lista:")
for i in range(0, 10):
    l1.append(int(input("Valor: ")))
print("Valores para a segunda lista:")
for i in range(0, 10):
    l2.append(int(input("Valor: ")))
for i in range(0, 10):
    soma.append(l1[i]+l2[i])
print("Lista 1:", l1)
print("Lista 2:", l2)
print("Soma das Listas:", soma)
