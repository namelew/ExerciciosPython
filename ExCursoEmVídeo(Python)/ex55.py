m = 0
mn = 0
for c in range(1, 6):
    p = float(input(f"Peso {c}ª Pessoa: "))
    if c == 1:
        m = p
        mn = p
    else:
        if p >= m:
            m = p
        if p <= mn:
            mn = p
print(f"Maior = {m} Kg\nMenor = {mn} Kg")
