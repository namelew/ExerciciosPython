print("Insira 3 números e escolha uma das opções")
n1 = float(input('Informe um valor: '))
n2 = float(input('Informe outro valor: '))
n3 = float(input('Informe outro valor: '))
print("Digite 1 para mostrá-los em ordem crescente")
print("Digite 2 para mostrá-los em ordem decrescente")
print("Digite 3 para mostrar o maior número entre eles")
opcao = int(input('Escolha a opção desejada:\n'))
if n2 > n1:
    temp = n1
    n1 = n2
    n2 = temp
if n3 > n1:
    temp = n1
    n1 = n3
    n3 = temp
if n2 < n3:
    temp = n2
    n2 = n3
    n3 = temp
if opcao == 1:
    print("\033[1;34m", n3, " \033[1;35m",  n2, "\033[1;31m ", n1)
elif opcao == 2:
    print("\033[1;31m ", n1, " \033[1;35m", n2, " \033[1;34m", n3)
elif opcao == 3:
    print(n1)
else:
    print("\033[1;31mErro! Escolha uma opção válida")
