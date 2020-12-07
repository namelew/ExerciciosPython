# Exercício
# Criar uma classe pessoa
# Atributos: nome, idade, peso, altura
# Métodos: envelhecer, engordar, emagrecer, crescer
# Criar um programa que recebe um objeto Pessoa(), a cada ano que passar ela envelhece um ano e se idade <= 21 deve crescer 0,5 cm por ano. 

class Pessoa(object):
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        anos = int(anos)
        self.idade += anos

    def engordar(self, npeso):
        self.peso += npeso

    def emagrecer(self, ppeso):
        self.peso -= ppeso

    def crescer(self, atganho):
        self.altura += atganho


nome = input('Nome: ')
idade = int(input("Idade: "))
peso = float(input("Peso: "))
altura = float(input("Altura(m): "))

amostra = Pessoa(nome, idade, peso, altura)

anos = int(input("Quantos anos teóricos? "))

for i in range(anos):
    if amostra.idade <= 21:
        amostra.crescer(0.005)
    amostra.envelhecer(1)

print("Após esse período:")
print(f"Idade: {amostra.idade} anos")
print(f"Altura: {amostra.altura:.2f} m")