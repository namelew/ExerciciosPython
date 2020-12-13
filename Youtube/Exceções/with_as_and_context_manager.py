# estrutura de um context manager(controla as estruturas, ex: with)
class SelfContextManager(object):
    def imprime(self, msg):
        print(msg)
    def __enter__(self): # inicializa a estrutura
        print("Entrando no bloco with")
        return self
    def __exit__(self, tipo, valor, traceback): # finaliza a estrutura caso haja um erro
        print(tipo) # erro
        print(valor) # valor errado
        print(traceback) # endereço/ponteiro da memória

with SelfContextManager() as teste: # era um try/exception automaticamente para tratamento de erros
    print("olá mundo")