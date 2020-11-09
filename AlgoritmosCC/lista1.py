# questão 1
print(28*45)
# questão 2
a1 = float(input())
a2 = float(input())
a3 = float(input())
print(f"Média: {(a1+a2+a3)/3}")
# questão 3
n = int(input())
print(f"Sucessor:{n+1}\nAntecessor:{n-1}")
# questão 4
n1 = int(input())
n2 = int(input())
print(f"Soma: {n1+n2}")
# questão 5
n = input(input())
print(f"Resultado: {n/3}")
# questão 6
r = float(input("Valor em real: R$ ").replace(',', '.'))
cot = float(input("Cotação do dolar: "))
print(f"Valor em Dolar: U$ {r/cot:.2f}")
# questão 7
d = int(input("Dias: "))
print(f"Foram produzidos no total, {(d)+(d*3)+(d*2,5)} portes em {d} dias")
# questão 8
n1 = float(input())
n2 = float(input())
n3 = float(input())
print(f"Média: {(n1*3+n2*2+n3*5)/10:.2f}")
# Desafio
h = int(input("Horas trabalhadas: ")
vl=float(input("Valor das Horas: R$ ").replace(',', '.'))
while True:
    p=input("Houve adiantamento?[Sim/Não]")[0].upper()
    if p == "S":
        a=float(input("Valor do adiantamento: R$ ").replace(',', '.'))
    elif p == "N":
        break
    print("Opção inválida! Digite novamente!")
print(
    f"Salário Bruto: R$ {h*vl:.2f}\nSalário Líquido:R$ {(h*vl) - (h*vl*0.08) - (h*vl*0,12) - a:.2f}")
