# customizando exceções
try:
    raise ValueError("spaw") # irá passar "spaw" como value de ValueError]
except ValueError as vm:
    print(vm)

# criando argumentos dentro de uma exceção
class ErroNaLinha(Exception):
    def __init__(self, linha):
        self.linha = linha # linha do erro
    def __str__(self):
        return f"Deu erro na linha {self.linha}"

raise ErroNaLinha(14) # testando a exceção