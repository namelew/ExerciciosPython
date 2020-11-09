#Calulo de Emprestimo
# input valor da casa, salário comprador, quantos anos pretende pagar
# processamento valor do empréstimo, sendo que V < 0.3*Salário senão será negado
# outpt negado ou aprovado
vc = float(input("Insira o valor da casa\nR$ "))
s = float(input("Insira o valor do salário do comprador\nR$ "))
a = int(input("Insira a quantidade de anos do financiamento\n"))
p = vc/(a*12)
print(f"Para pagar uma casa de R$ {vc:.2f} em {a} anos, as prestações serão de R$ {p:.2f}")
if p < s*0.3:
    print("\033[1;34mEmpréstimo Aprovado")
else:
    print("\033[1;31mEmpréstimo Negado")
