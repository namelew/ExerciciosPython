from datetime import date
ano = date.today().year
funcionario = {
    'nome': input("Nome: "),
    'sexo': input("Sexo: ").upper()[0],
    'anon': int(input("Data de Nascimento: ")),
    'carteirat': int(input("Carteita de Trabalho(0 caso não possua): ")),
    'anoc': 2,
    'sal': 2.5
}
print(f"Nome Funcionário: {funcionario['nome']}")
print(f"Sexo: {funcionario['sexo']}")
idade = ano - funcionario['anon']
print(f"Idade: {idade} anos")
print(f"CT: {funcionario['carteirat']}")
if funcionario['carteirat'] > 0 and funcionario['carteirat'] != 0:
    funcionario['anoc']: int(input("Ano de Contratação: "))
    funcionario['sal']: float(input("Salário: R$ "))
    if funcionario['sexo'] == 'M':
        anosc = funcionario['anoc'] + 20
        if idade < 65:
            print(f"Aposentadoria: 65 anos")
        else:
            print(f"Aposentadoria: {anosc+idade} anos")
    else:
        anosc = funcionario['anoc'] + 15
        if idade < 62:
            print(f"Aposentadoria: 62 anos")
        else:
            print(f"Aposentadoria: {anosc+idade} anos")
else:
    print("Erro!")
