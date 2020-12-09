"""
Escreva um programa de bancos que possua:
    Uma classe Banco com os atributos
    - private total
    - public TaxaReserva
    - private reservaExigida

    E métodos
    - public podeFazerEmprestimo(valor) --> bool
    - public MudaTotal(valor)

E uma classe conta com os atributos
    - private saldo
    - private ID
    - private senha

    E métodos
    - public deposito(senha, valor)
    - public saque(senha, valor)
    - public podeReceberEmprestimo(valor) --> bool
    - public saldo --> float
"""
class Banco(object):
    __total = 10000 # atributo estático(private)
    TaxaReserva = 0.1 # atributo dinâmico(public)
    # ambos também podem ser utilizado em métodos
    __reservaExigida = __total * TaxaReserva

    def podeFazerEmprestimo(self, valor):
        if valor <= Banco.__total:
            return True
        return False

    def MudarTotal(self, valor):
        Banco.__total += valor

class Conta(Banco):
    def __init__(self, ID, senha, saldo):
        super().MudarTotal
        self.__ID = ID
        self.__senha = senha
        self.__saldo = saldo
        super().MudarTotal(saldo)
    
    def deposito(self, senha, valor):
        s = senha
        v = valor
        if self.__senha == s:
            self.__saldo += valor
            super.MudarTotal(valor)
            return
        print("Senha Incorreta")
        s = input("Senha: ")
        v = float(input("Depósito: "))
        return self.deposito(s, v)
    
    def saque(self, senha, valor):
        s = senha
        v = valor
        if self.__senha == s:
            if super().podeFazerEmprestimo(valor):
                if self.podeReceberEmprestimo:
                    self.__saldo -= valor
                    super.MudarTotal(-valor)
                    return
                print("Saldo Insuficiente")
                return
            print("Tesouro Insuficiente")
            return
        print("Senha Incorreta")
        s = input("Senha: ")
        v = float(input("Saque: "))
        return self.saque(s, v)

    def podeReceberEmprestimo(self, valor):
        if valor <= self.__saldo:
            return True
        return False

    def saldo(self):
        return float(self.__saldo)
