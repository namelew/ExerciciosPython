# raise: devolve uma exceção("induz" um erro)
try:
    raise ValueError
except ValueError:
    print("Gerei um erro")

# criando uma exceção
class ValorRepetidoError(Exception):
    def __init__(self, n):
        self.n = n
    def __str__(self):
        return f"O valor {self.n} já foi digitado"

lista = []
for i in range(3):
    while True:
        try:
            num = int(input("Número: "))
            break
        except ValueError:
            print("Valor inválido! Digite um número inteiro")
    if num not in lista:
        lista.append(num)
    else:
        raise ValorRepetidoError(num)