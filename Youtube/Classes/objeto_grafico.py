# Exercício de Herança/Polimorfismo
# Escrever uma classe pai Objeto Gráfico(At: cor_de_preenchimento(int), preenchida(bool), cor_contorno(int))
# depois criar três classes Retângulo(at: base, altura), Circulo(at: raio) e Triangulo(at: base,altura), 
# todas com os métodos área e perimetro. Elas devem ser subclasses da classe Objeto Gráfico
class ObjetoGrafico(object):
    def __init__(self, cor_de_preenximento, preenxida, cor_de_contorno):
        self.cor_de_preenximento = cor_de_preenximento
        self.preenxida = preenxida
        self.cor_de_contorno = cor_de_contorno

class Retangulo(ObjetoGrafico):
    def __init__(self, base, altura, cor_de_preenximento, preenxida, cor_de_contorno):
        super().__init__(cor_de_preenximento, preenxida, cor_de_contorno)
        self.base = base
        self.altura = altura
        self.cores = ['branco', 'azul', "vermelho"]

    def perimetro(self):
        return self.base*2 + self.altura*2

    def area(self):
        return self.base*self.altura

class Circulo(ObjetoGrafico):
    def __init__(self, raio, cor_de_preenximento, preenxida, cor_de_contorno):
        super().__init__(cor_de_preenximento, preenxida, cor_de_contorno)
        self.raio = raio

    def perimetro(self):
        return 2 * 3.14 * self.raio

    def area(self):
        return 3.14 * self.raio ** 2

class Triangulo(ObjetoGrafico):
    def __init__(self, base, altura, cor_de_preenximento, preenxida, cor_de_contorno):
        super().__init__(cor_de_preenximento, preenxida, cor_de_contorno)
        self.base = base
        self.altura = altura

    def perimetro(self):
        return self.base + self.altura * 2

    def area(self):
        return (self.base*self.altura)/2

tri = Triangulo(50, 25, 2, False, 3)
ret = Retangulo(50, 25, 2, False, 3)
ci = Circulo(50, 2, False, 3)

print(isinstance(tri, Triangulo)) # Monstra se um objeto é uma instância de terminada classe
print(issubclass(Retangulo, ObjetoGrafico)) # Monstra se uma class é subclass de certa class
print(isinstance(ret, Triangulo))