from ex108 import moeda
p = float(input("Digite o preço: R$ "))
print(f"Dobro de {moeda.moeda(p)}: {moeda.moeda(moeda.dobro(p))}")
print(f"Metade de {moeda.moeda(p)}: {moeda.moeda(moeda.metade(p))}")
print(f"Aumento de 10% de {moeda.moeda(p)}: {moeda.moeda(moeda.aumentar(p, 10))}")
print(f"Diminuição de 15% de {moeda.moeda(p)}: {moeda.moeda(moeda.diminuir(p, 15))}")
