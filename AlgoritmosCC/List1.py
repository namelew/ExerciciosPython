#Questão 1
temp = float(input("Digite uma temperatura em graus Fahrenheit\n"))
print(f"{temp} ºF convertida para Celsius equivale a {(temp-32)/1.8:.2f} ºC")

#Questão 2
mont = float(input("Digite o montante em reais que será convertida para dolar e euro\n"))
print(f"Dólar = U$ {mont/5.27:.2f}\nEuro = E$ {mont/5.71:.2f}")

#Questão 3
np = int(input("Digite o número de dias:\n"))
print(f"Trabalhando por {np} dias a usina é capaz de produzir {np*6.5:0.f} pontes")

#Questão 4
pt = int(input("Digite a quantidade de peças de tecidos\n"))
print(f"A partir de {pt} peças de tecidos a fábrica pode produzir {pt*5} ", end='')
print(f"calças tendo um desperdício de {(pt*11)*0.15:.2f} m² de tecido")

#Questão 5
from math import floor
alg = int(input("Digite a quantidade de algodão que será ultilida, em kilogramas\n"))
print(f"Utilizando {alg} Kg de algodão é possível fabricar {alg*1000/100*0.95:.0f} camisetas", end='')
print(f" e com os {(alg*1000)*0.05} g que sobraram podemos fazer mais {floor(((alg*1000)*0.05)/100*0.95)} camisetas")

#Questão 6
ad = float("Digite a medida da aresta direita\n")
ae = float(input("Digite a medida da aresta esquerta\n"))
base = float(input("Digite a medida da base\n"))
print(f"O perímetro desse triângulo é de {ad+ae+base} u")

#Questão 7
n = int(input("Digite a quantidade total de horas\n"))
v = float(input("Digite o valor das horas trabalhadas\nR$ "))
a = float(input("Digite o valor do vale, se houver.\nR$ "))
N = n*v
print(f"Salário Bruto = R$ {N:.2f}\nSalário Líquido = R$ {N-(N*0.08)-(N*0.12)-a:.2f}")

#Questão 8
n1 = float(input("Digite a nota da primeira prova\n"))
n2 = float(input("Digite a nota da segunda prova\n"))
n3 = float(input("Digite a nota da terceira prova\n"))
print(f"A nota do aluno será {((n1*3)+(n2*2)+(n3*5))/10} pontos")

#Questão 9
n = int(input("Digite o número de caracteres do texto\n"))
v = float(input("Digite a velocidade de impressão da impressora, em caracteres por segundo.\n"))
print(f"A impressora levará {n/v/60:.2f} minutos para imprimir o texto completo")

#Questão 10
nome = input("Qual atividade física deseja práticar?\n").strip()
perda = float(input("Digite o valor calórico que será perdido a cada 1h de prática da atividade física:\n"))
desejado = float(input('Digite a quantidade de calorias que deseja perder:\n'))
print(f"Serão necessários {desejado/perda:.2f} horas de prática de {nome.lower()} para se obter esse resultado")
