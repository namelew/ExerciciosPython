from ex107 import moeda
p = float(input("Digite o preço: R$ "))
print(f"Dobro de {p}: {moeda.dobro(p)}")
print(f"Metade de {p}: {moeda.metade(p)}")
print(f"Aumento de 10% de {p}: {moeda.aumentar(p, 10)}")
print(f"Diminuição de 15% de {p}: {moeda.diminuir(p, 15)}")
