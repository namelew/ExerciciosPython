# Exercício
# Criar uma classe ponto com os atributos x e y
# Criar uma classe retangulo com os atributos largura, altura e vertice inicial(obj. Ponto)
# O objetivo é utilizando, chamadas de classes dentro de classes, fazer, sempre que alt ou lar for alterado
# O método encontrarCentro() sempre encontrar o centro.

class Ponto(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def pinicial(self):
        print(f"Coordenada Inicial: (x={self.x}, y={self.y})")

    def pcentro(self):
        print(f"Centro: (x={self.x}, y={self.y})")

class Retangulo(object):
    def __init__(self, largura, altura, vertinicial):
        self.largura = largura
        self.altura = altura
        self.vertinicial = vertinicial

    def encontraCentro(self):
        self.centro = [self.largura/2, self.altura/2]
        self.vertinicial.x = self.centro[0]
        self.vertinicial.y = self.centro[1]

vertice = Ponto(200,100)
ret = Retangulo(200, 100, vertice)
ret.vertinicial.pinicial()
ret.encontraCentro()
ret.vertinicial.pcentro()
ret.largura = 400
ret.altura = 250
ret.encontraCentro()
ret.vertinicial.pcentro()