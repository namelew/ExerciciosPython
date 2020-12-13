# Raise from
# try:
#     n = 1/0
#     a = int(n)
# except Exception as e:
#     raise ValueError from e # estou dizendo que "e" causou ValueError
# ASSERT
while True:
    try:
        num = int(input("Digite um número entre 1 e 20: "))
    except ValueError:
        print(f"Erro!! {num} não é um valor válido!")
    except:
        print("Entrada Inválida!!!!")
    else:
        break

teste = True

if not 1 <= num <= 20:
    teste = False

assert teste, num # o python dará erro caso o valor dessas variáveis seja != do esperado

if __debug__:
    if not teste:
        raise AssertionError(num) # nesse caso o erro é criado se teste == False

# Exemplo de uso do assert

def raiz(x):
    assert x > 0, 'x tem que ser maior que 0'
    return x ** 1/2

raiz(-1)