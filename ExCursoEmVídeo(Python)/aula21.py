#ajuda interativa
#help(input)
#outra maneira
#print(input.__doc__)
#docstring: string de documentação
#def cont(i,f,p):
    #docstring cont
    #"""
    #->Faz uma contagem e mostra na tela
    #:param i: inicio da contagem
    #:param f: fim da contagem
    #:param p: progressão ou passo da contagem
    #:return: sem retorno
    #"""
    #c = i
    #while c <= f:
        #print(f"{c} ", end='')
        #c += p
    #print("FIM")
#parâmetros opcionais:
#def soma(a, b, c=0):
#    s = a + b + c
 #   print(s)
#def funcao():
    #global n1 usa a val global em vez de criar uma local
#    n1 = 4
#    print("N1 dentro vale", n1)
#retornar valores
#def soma(a=0, b=0, c=0):
#    s = a + b + c
#    return s

#help(cont)
#r1 =soma(5, 6, 2)
#r2 =soma(9, 2)
#r3 =soma(7)
#print(f"Os resultados foram {r1}, {r2}, {r3}")
#n1 = 2
#funcao()
#print("N1 fora vale", n1)
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input("Número: "))
print(f"O fatorial de {n} é {fatorial(n)}")
