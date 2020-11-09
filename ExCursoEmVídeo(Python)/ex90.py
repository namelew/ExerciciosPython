aluno = {
    'nome': input("Nome: "),
    'media': float(input("Média: "))
}
if aluno['media'] >= 7:
    aluno['st'] = 'Aprovado'
else:
    aluno['st'] = 'Reprovado'
print(f"Nome: {aluno['nome']}")
print(f"Média: {aluno['media']:.1f}")
print(f"Situação: {aluno['st']}")
