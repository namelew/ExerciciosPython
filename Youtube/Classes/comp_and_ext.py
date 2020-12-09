# Comparações e Extensões
class Conta(object):
    def __init__(self, Id, saldo):
        self.Id = Id
        self.saldo = saldo

    def saque(self, valor):
        self.saldo -= valor

    def deposito(self, valor):
        self.saldo += valor

# Comparações
# Configurando comparações(Métodos Especiais):
# __le__ x<=y, __eq__ x==y, __ge__ x>=y, __lt__ x<y, __gt__ x>y, __ne__ x!=y
itau = Conta(123, 300)
bb = Conta(123, 300)
# mesmo elas sendo iguais será retornado false.
print(itau == bb) # esse teste, em objetos, testa se os ponteiros são iguais não os valores
# para se alterar isso utilizasse os métodos acima

# Extensão: Tratasse de alterar o funcionamento de uma função nativa do python
class Lista(list): # class filha de list
    def sort(self): # o método sort() foi escrito
        print("Arrumei a lista")

Lis = Lista()
Lis.sort() # A função sort foi alterada localmente, por causa do polimorfismo