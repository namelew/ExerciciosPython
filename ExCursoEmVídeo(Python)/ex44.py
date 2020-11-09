#calcular desconto
#à vista dinheiro/cheque == 10% de desconto
#à vista cartão == 5%  de desconto
#2x cartão == preço normal
#3x ou mais == 20% de juros
print("\033[1;34m-=-\033[0m"*20)
print(" "*25, "\033[1;33mCAIXA")
print("\033[1;34m-=-\033[0m"*20)
p = float(input("Insira o preço do produto\nR$ "))
print("Formas de Pagamento:")
print("1: À vista no dinheiro ou cheque")
print("2: À vista no cartão")
print("3: 2x no cartão")
print("4: 3x ou mais vezes no cartão:")
f = int(input("Insira a forma de pagamento: "))
if f == 1:
    print("O produto terá um desconto de 10% e", end='')
    print(f" seu preço final será de \033[1;34mR$ {p * 0.90:.2f}")
elif f == 2:
    print("O produto terá um desconto de 5% e", end='')
    print(f" seu preço final será de \033[1;34mR$ {p * 0.95:.2f}")
elif f == 3:
    print("Não haverá acrescimos ou descontos no preço do produto.", end='')
    print(f" Logo seu preço será \033[1;34mR$ {p:.2f}")
elif f == 4:
    pr = int(input("Quantas vezes? "))
    vp = p*1.20/pr
    print(f"Haverá um acrescimo de 20% no valor do produto, o valor das parcelas será \033[1;34mR$ {vp:.2f}", end='')
    print(f"\033[0m e o preço final será \033[1;34mR$ {p*1.20:.2f}")
else:
    print("\033[1;31mErro!Insira uma opção válida")
