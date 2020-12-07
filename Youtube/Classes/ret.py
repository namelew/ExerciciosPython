# Execício
# Criar uma classe que modele um retângulo
# Atributos: Base, Altura
# Métodos: Mudar valor dos lados, retornar valor dos lados, calcular área, calcular perímetro.
# Crie um programa que utilize essas classes onde o usuário digita as dimensões do local e calcula a quantidade de pisos necessários para ele.

class Retangulo(object):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudarLados(self, novaBase, novaAltura):
        self.base = novaBase
        self.altura = novaAltura
        print(f"Base alterada para {novaBase} e altura, para {novaAltura}")

    def retornarLados(self):
        lados = [self.base, self.altura]
        return lados

    def calcularArea(self):
        area = self.base * self.altura
        return area

    def calculaPer(self):
        perimetro = (self.base * 2) + (self.altura * 2)
        return perimetro 

base = float(input("Largura do terreno[m]: "))
altura = float(input("Comprimento do terreno[m]: "))
ta = int(input("Área dos Azulejos[m²]: "))

terreno = Retangulo(base, altura)

at = terreno.calcularArea()
qa = at/ta

print(f"Serão necessários {qa:.0f} azulejos para terminar cobrir o terreno.")
