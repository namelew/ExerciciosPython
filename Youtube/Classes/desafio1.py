class Carro:
    def __init__(self, marca, motor, consumo):
        self.marca = marca
        self.motor = motor
        self.consumo = consumo

    def Ligar(self):
        print("Estou ligando")

    def Informacoes(self):
        print(self.marca, self.motor, self.consumo)

    def Desligar(self):
        print("Estou desligando")

    def Corrida(self, km):
        print(f"Percorrendo {km} km, eu consumirei um total de {float(self.consumo) * km} litros de combustível.")


carro1 = Carro('Gol', '7 Cavalos', 4)
carro1.Ligar()
carro1.Informacoes()
carro1.Corrida(12)
carro1.Desligar()

