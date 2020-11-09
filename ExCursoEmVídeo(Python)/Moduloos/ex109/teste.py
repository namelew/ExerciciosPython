from ex109 import moeda
p = float(input("Digite o preço: R$ "))
print(f"Dobro de {moeda.moeda(p)}: {moeda.dobro(p, True)}")
print(f"Metade de {moeda.moeda(p)}: {moeda.metade(p, True)}")
print(f"Aumento de 10% de {moeda.moeda(p)}: {moeda.aumentar(p, 10, True)}")
print(f"Diminuição de 15% de {moeda.moeda(p)}: {moeda.diminuir(p, 15, True)}")
