t = (int(input("Número 1: ")),
     int(input("Número 2: ")),
     int(input("Número 3: ")),
     int(input("Número 4: ")))
print(f"O número 9 apareceu {t.count(9)} vezes;")
if 3 in t:
    print(f"O 3 apareceu na {t.index(3)+1}ª posição;")
else:
    print("O 3 não foi digitado;")
print(f"E dentro da tupla os valores pares foram: ", end='')
for n in t:
    if n % 2 == 0:
       print(n, end=' ')
