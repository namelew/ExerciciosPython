#Conversor bases numéricas
#input valor decimal, escolha da base numérica a qual o valor será convertido
#1 == Binário, 2 == Octal, 3 == Hexadecimal
#processamento conversão da base
#output valor convertido
n = int(input("Digite um número inteiro: "))
print('''Escolha uma base para conversão:
[ 1 ] converter para binário
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal''')
o = int(input("Opção: "))
if o == 1:
    print(f"{n} convertido para binário é {bin(n)[2:]}")
elif o == 2:
    print(f"{n} convertido para octal é {oct(n)[2:]}")
elif o == 3:
    print(f"{n} convertido para hexadecimal é {hex(n)[2:]}")
else:
    print("\033[1;31mDigite uma opção válida")
