#ler o salário de um funcionário e calcular seu aumento
#Salários > R$ 1250,00, aumento de 10%
#Salários <= R$ 1250,00, aumento de 15%
print('-'*20, "Calculando o Aumento", '-'*20)
s = float(input("Digite o salário do funcionário\n"))
if s > 1250.00:
    print(f"O funcionário receberá um aumento de R$ {s*0.10:.2f} em seu salário e seu novo salário será ", end='')
    print(f"R$ {(s*0.10)+s:.2f}")
else:
    print(f"O funcionário receberá um aumento de R$ {s*0.15:.2f} em seu salário e seu novo salário será ", end='')
    print(f"R$ {(s * 0.15) + s:.2f}")
