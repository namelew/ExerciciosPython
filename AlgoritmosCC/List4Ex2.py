h = float(input("Hectares: "))
p = float(input("Preço Tonelada(Soja): R$ "))
t = h * 3
print(f"Serão produzidos {t:.1f} toneladas.", end='')
if t >= 10:
    print(f" O faturamento será de R$ {(t*p):.2f}.", end='')
    print(f" Com um incentivo de R$ {(t*p)*0.05:.2f}.")
else:
    print(f" O faturamento será de R$ {t*p:.2f}. ", end='')
    print("Com um incentivo de R$ 0.")
