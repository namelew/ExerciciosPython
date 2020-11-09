#questão 1
qm = int(input("Quantidade de garotos: "))
qf = int(input("Quantidade de garotas: "))
t = qf + qm
print(f"Porcentagem de garotos dessa sala é {(qm/t)*100:.2f} %")
print(f"Porcentagem de garotas dessa sala é {(qf/t)*100:.2f} %")
#questão 2
n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
n3 = float(input("Terceira nota: "))
m = (n1+n2+n3)/3
print(f"Média: {m:.2f}")
if m >= 6:
    print("Aprovado")
else:
    print("Reprovado")
    if n2 < n1 and n2 < n3:
        sup = n2
        n1 = n2
        n2 = sup
    elif n3 < n1 and n3 < n2:
        sup = n3
        n1 = n3
        n3 = sup
    n1 = float(input("Nova nota: "))
    m = (n1 + n2 + n3) / 3
    print(f"Nova média: {m:.2f}")
#questão 3
n = float(input("Nota: "))
a = input("Entregou todas as atividades(s/n)? ")
if n >9:
    print("Conceito A")
elif 7 < n <= 9:
    if a == "s":
        print("Conceito A")
    elif a == "n":
        print("Conceito B")
elif 4 < n <= 7:
    if a == "s":
        print("Conceito B")
    elif a == "n":
        print("Conceito C")
elif 0 < n <= 4:
    if a == "s":
        print("Conceito C")
    elif a == "n":
        print("Conceito D")
#questão 4
from time import sleep
print("\033[1;34m-=-\033[0m"*20)
print("\033[1;30;mMáquina do Tempo")
print("\033[1;34m-=-\033[0m"*20)
sleep(1)
print("Você tem 3 créditos de viagem")
sleep(1)
print("Cada crédito equivale a uma viajem conforme a tabela: ")
sleep(1)
print("\033[1;34m-=-\033[0m"*20)
sleep(1)
print("\033[1;35mCrédito 1: Ida\nCrédito 2: Volta\nCrédito 3: Ida ou Volta")
print("\033[1;34m-=-\033[0m"*20)
sleep(2)
print("Digite a quantidade de anos que deseja viajar!")
c1 = int(input("Crédito 1: "))
c2 = int(input("Crédito 2: "))
c3 = int(input("Crédito 3: "))
sleep(1)
print("\033[4;35mProcessando...\033[0m")
sleep(1)
if c1 and c2 == 0 or c3 and c2 == 0:
  print("\033[1;31mÉ impossível voltar")
elif c2 + c1 == c3 or c2 + c3 == c1 or c1 + c3 == c2:
  print("\033[1;36mÉ possível voltar")
elif c2 - c1 == c3 or c1 + c3 == c2 or c2 - c3 == c1:
  print("É possível voltar")
elif c2 == c1 or c1 == c3 or c3 == c2:
  print("É possível voltar")
else:
  print("\033[1;31mÉ impossível voltar")
#questão 5
n = int(input("Insira um número: "))
if n % 5 == 0 and n % 11 == 0:
    print(f"{n} é divisivel por 5 e 11")
else:
    if n % 5 == 0:
        print(f"{n} é divisivel apenas por 5")
    elif n % 11 == 0:
        print(f"{n} é divisivel apenas por 11")
    else:
        print(f"{n} não é divisel por 5 ou 11")
#questão 6
c1 = int(input("Votos: C1: "))
c2 = int(input("Votos: C2: "))
c3 = int(input("Votos: C3: "))
if c1 > c2 and c1 > c3:
    print("Vencedor: \033[1;34mC1")
elif c2 > c1 and c2 > c3:
    print("Vencedor: \033[1;34mC2")
elif c3 > c1 and c3 > c2:
    print("Vencedor: \033[1;34mC3")
else:
    print("\033[1;31mNão houve vencedores!")