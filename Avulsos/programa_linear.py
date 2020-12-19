def CalculaRest(x, y):
    # Criando as Restrições
    pontos = [x, y]

    tabuas = 5 * pontos[0] + 20* pontos[1]
    horas = 10 * pontos[0] + 15 * pontos[1]
    
    if tabuas <= 400 and horas <= 450:
        return True
    return False
def Maximo():
    # Encontrando o ponto máximo
    maior = 0
    vertices = [[0, 20], [45, 0], [24, 14]]
    for v in vertices:
        lucro = 180 * v[0] + 320 * v[1]
        if lucro > maior:
            maior = lucro
            vm = v.copy()
    return maior, vm
# recebendo valores quaisquer    
cad = int(input("Quant. Cadeiras: "))
mesas = int(input("Quant. Mesas: "))
# filtrando por restrições
if CalculaRest(cad, mesas):
    # lucro a partir dos valores quaisquer
    lucro = cad * 180 + mesas * 320
    maior, pm = Maximo()
    print("-" * 25)
    print(f"Cadeiras: {cad}\nMesas: {mesas}\nLucro Total: R$ {lucro:.2f}")
    # lucro máximo que pode ser obtido
    print("-" * 25)
    print(f"Cadeiras: {pm[0]}\nMesas: {pm[1]}\nLucro Máximo: R$ {maior:.2f}")
    print("-" * 25)
else:
    print("As quantidades não respeitão as restrições de horas e material")