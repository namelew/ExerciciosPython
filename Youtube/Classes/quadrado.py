# Exércicio
# Classe quadrado que pode mudar o lado do quadrado, retornar esse valor e calcular sua área
class Quadrado(object):
    def __init__(self, lado):
        self.lado = lado

    def mudaLado(self, x):
        self.lado = float(x)
        print(f"O valor do lado foi alterado para {x} cm")

    def calculaArea(self):
        self.area = self.lado ** 2
        print(f"A área desse quadrado é {self.area} cm")

    def retornaLado(self):
        return self.lado
    
qua = Quadrado(20)

print(f"O Quadrado possui lados de {qua.retornaLado()} cm")

op = input("Deseja alterar?[S/N] ").upper()[0]
if op == 'S':
    novoLado = input("Novo Lado: ")
    qua.mudaLado(novoLado)
qua.calculaArea()