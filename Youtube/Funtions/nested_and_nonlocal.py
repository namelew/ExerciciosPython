# nested
# função declarada dentro de outra função
def f1():
    x = 3000
    def f2():
        print(x)
    f2()
# uso 1:
def exp(n):
    def base(x):
        return x ** n
    return base
f = exp(3) # define o valor de n e f se torna um espelho de base
print(f(10)) # 10 elevado a 3

# nonlocal
# permite alterar o valor de uma variável sem inferir no valor inicial da mesma
def bas():
    começo = 0
    def incremento():
        nonlocal começo # indica que a variavel começo existe fora da função
        print(começo)
        começo += 1
    return incremento
b = bas()
b() # 0
b() # 1
b() # 2 # ps: o valor de começo dentro de bas() continua sendo 0