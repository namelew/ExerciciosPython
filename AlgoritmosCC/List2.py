#ex1
print("-=-"*20)
print("Calculando Salário de Funcionários")
print("-=-"*20)
h = int(input("Horas Trabalhadas: "))
vh = float(input("Valor da Hora: R$ "))
salario = h*vh if h <= 200 else (h*vh)+((h*vh)*0.05) #ou salario += 1.05
print(f"Salário: R$ {salario:.2f}")

#ex2
q = int(input("Quantidade Comprada: "))
v = q * 0.30 if q <= 12 else q * 0.25
print(f"Valor a pagar: R$ {v:.2f}")

#ex3
from time import sleep
p = float(input("Preço do produto: R$ "))
print("1 para pagamento à vista e 2 para pagamento à prazo")
sleep(1)
op = int(input("Forma de pagamento: "))
if op == 1:
    print(f"Preço à vista: R$ {p*0.95}")
if op == 2:
    print(f"Preço à vista: R$ {p*1.1}")
if op != 1 and op != 2:
    print("Erro! Por Favor, insira 1 ou 2 para escolher uma forma de pagamento")

#ex4
vja = int(input("Votos João da Chape: "))
vjs = int(input("Votos José da Chape: "))
if vja > vjs:
    print("João da Chape ganhou!")
if vjs > vja:
    print("José da Chape ganhou!")
if vja == vjs:
    print("Houve empate!")

#ex5
a = float(input("1º Número: "))
b = float(input("2º Número: "))
print("São múltiplos" if a % b == 0 or b % a == 0 else "Não são múltiplos")

#ex6
inicio = int(input("Início: "))
fim = int(input("Fim: "))
if inicio > 24 or fim > 24:
    print("Erro! Digite um horário válido")
if inicio <= 12 and fim > 12:
    print(f"Duração: {fim - inicio:.0f} horas")
if inicio >= 12 and fim < 12:
    print(f"Duração: {(24-inicio)+fim} horas")

#ex7
a = int(input("N1: "))
b = int(input("N2: "))
c = int(input("N3: "))
d = int(input("N4: "))
p = 0
n = 0
if a >= 0:
    p += 1
if b >= 0:
    p += 1
if c >= 0:
    p += 1
if d >= 0:
    p += 1
if a < 0:
    n += 1
if b < 0:
    n += 1
if c < 0:
    n += 1
if d < 0:
    n += 1
print(f"Positivos: {p} Negativos {n}")

#ex8
p = int(input("Posição: "))
if p <= 5:
    print("Top 5")
if 5 < p <= 10:
    print("Top 10")
if 10 < p <= 20:
    print("Top 20")
if 20 < p <= 30:
    print("Top 30")
if 30 < p <= 100:
    print("Top 100")
if 100 < p:
    print("Outras posições")

#ex9
a = float(input("Altura: "))
p = float(input("Peso: "))
imc = p/a**2
if imc < 18.50:
    print(f"Imc: {imc:.2f} (Abaixo do Peso)")
if 18.50 < imc <= 24.90:
    print(f"Imc: {imc:.2f} (Normal)")
if 24.90 < imc <= 29.90:
    print(f"Imc: {imc:.2f} (Sobrepeso)")
if imc > 29.90:
    print(f"Imc: {imc:.2f} (Obeso)")

#ex10
id = int(input("Idade: "))
if id < 16:
    print("Não pode votar")
if 18 <= id <= 70:
    print("Voto obrigatório")
if id == 16 or id == 17 or id > 70:
    print("Voto facultativo")
