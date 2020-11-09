#média aluno
#input n1,n2
#processamento (n1+n2)/2
#m<5 : aluno reprovado
#m>=7 : aluno aprovado
#5<=m<7: aluno de recuperação
n1 = float(input("Insira a primeira nota "))
n2 = float(input("Insira a segunda nota "))
m = (n1+n2)/2
if m >= 7:
    print("Aluno aprovado")
elif 5 <= m < 7:
    print("Aluno de recuperação")
else:
    print("Aluno reprovado")