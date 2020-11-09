va = 60
vb = 52
h = 1
while True:
    df = 45 + (vb * h) - (va * h)
    if df <= 0:
        break
    h += 1
print(f"O veículo A alcançará o veículo B em {h} horas!")