#tempo = int(input("Quantos anos tem seu carro?\n"))
#condição simplificada print("Carro Novo" if tempo <=3 else "Carro Velho")
#print("----FIM----")
n1 = float(input("Digite a primeira nota\n"))
n2 = float(input("Digite a segunda nota\n"))
n3 = float(input("Digite a terceira nota\n"))
m = (n1+n2+n3)/3
print(f"A média do aluno foi {m:.2f}")
print("Aluno aprovado" if m>=7 else "Aluno reprovado")
