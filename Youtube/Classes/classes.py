# class
# sintaxe

# Marca, Memoria RAM, Placa de Vídeo
class Computador:
    def __init__(self, marca, ram, placa):
        self.marca = marca
        self.ram = ram
        self.placa = placa

    def Ligar(self):
        print("Estou ligando")

    def Desligar(self):
        print("Estou desligando")

    def Exibir(self):
        print("Exibindo Informações do Computador")
        print(self.marca, self.ram, self.placa)


computador1 = Computador('Asus', '8 GB', 'Nvidia')
computador1.Ligar()
computador1.Exibir()
computador1.Desligar()
print()
computador2 = Computador('Apple', '12 GB', 'Amd')
computador2.Ligar()
computador2.Exibir()
computador2.Desligar()
print()
computador3 = Computador('MaC', '16 GB', 'ATM')
computador3.Ligar()
computador3.Exibir()
computador3.Desligar()
