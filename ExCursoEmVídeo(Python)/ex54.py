from datetime import date
at = date.today().year
mn = 0
m = 0
for c in range(1, 7):
    an = int(input(f"Data de aniversário, {c}ª pessoa: "))
    i = at - an
    if i >= 21:
        m += 1
    else:
        mn += 1
print(f"Dentro dessas 6 pessoas, {m} são maiores de idade e {mn} não são.")