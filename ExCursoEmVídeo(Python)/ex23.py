#jeito matemático de resolver
#num = int(input("Digite um número entre 0 e 9999\n"))
#u = num // 1 % 10
#d = num // 10 % 10
#c = num // 100 % 10
#m = num // 1000 % 10
#print(f"unidade = {u}\ndezena = {d}\ncentena = {c}\nmilhar = {m}")
n = int(input('Digite um número entre 0 e 9999:\n'))
n2 = str(int(10000 + n))
print(f"O número {n} possui:")
print(f'{n2[1]} milhares.')
print(f'{n2[2]} centenas.')
print(f'{n2[3]} dezenas.')
print(f'{n2[4]} unidades.')
