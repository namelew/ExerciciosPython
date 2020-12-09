# Métodos e Atributos Especiais

class Conta(object):
    def __init__(self, Id, saldo):
        self.Id = Id 
        self.saldo = saldo

    def __str__(self):
        """Retorna uma string de descrição do objeto Conta"""
        return f"Id: {self.Id}\nSaldo: {self.saldo}"

    def __add__(self, outro):
        """ Habilita obj + obj. No caso, essa soma resultara no aumento do saldo de um """
        self.saldo += outro.saldo
    
    def __sub__(self, outro):
        """ Habilita obj - obj. Redunção do saldo"""
        self.saldo -= outro.saldo

    def __mult__(self, outro):
        """Habilita obj * obj. Multiplicação de saldo"""
        self.saldo *= outro.saldo

    def __div__(self, outro):
        """Habilita obj/obj. Divisão de saldo"""
        self.saldo /= outro.saldo

    def __call__(self, x):
        """Permite que a instância de Conta também possa ser chamada"""
        print(x)


bradesco = Conta(123, 500)
itau = Conta(341, 10)
print(bradesco) # o __str__ é chamado sem precisar chamar pela instância

bradesco + itau # uso do __add__
print(bradesco)

bradesco - itau # uso do __sub__
print(bradesco)

# multi = bradesco * itau # uso do __mult__ // Não funcionou por algum motivo
# print(bradesco)
# bradesco/itau # uso do __div__ // Mesma coisa aqui
# print(bradesco)

print(Conta.__bases__) # monstra a superclasse  direta de uma classe

print(bradesco.__add__.__doc__) # retorna a docstrig de algum objeto/método/classe

print(callable(Conta)) # retorna se determinado objeto pode ser chamado dentro do código

bradesco(12) # chamando o objeto bradesco