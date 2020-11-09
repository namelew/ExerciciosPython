n10 = ('zero', "um", 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
n11 = ('onze', 'doze', 'treze', 'quatorze', 'quize', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n20 = n10 + n11
n = -1
while n not in range(0, 21):
    n = int(input("Digite um valor entre 0 e 20: "))
print(f"Você escreveu o número {n20[n]}.")
