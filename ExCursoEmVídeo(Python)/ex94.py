pessoas = []
mulheres = []
pam = []
s = 0
registro = {
}
while True:
    registro['nome'] = input("Nome: ").capitalize()
    registro['idade'] = int(input("Idade: "))
    s += registro['idade']
    registro['sexo'] = input("Sexo[M/F]: ")[0].upper()
    if registro['sexo'] in "Ff":
        mulheres.append(registro['nome'])
    while registro['sexo'] not in "MmFf":
        print("Erro! Digite M ou F!")
        registro['sexo'] = input("Sexo[M/F]: ")[0].upper()
    pessoas.append(registro.copy())
    c = input("Deseja Continuar[S/N]? ")[0]
    while c not in "NnSs":
        print("Erro! Digite Apenas S ou N.")
        c = input("Deseja Continuar[S/N]? ")[0]
    if c in "Nn":
        break
for p in pessoas:
    if p['idade'] > s/len(pessoas):
        pam.append(p['nome'])
        pam.append(p['idade'])
print("-="*30)
print(f"A) Ao todo temos {len(pessoas)} pessoas cadastradas.")
print(f"B) A média das idades foi {s/len(pessoas):.2f} anos.")
print("C) As mulheres cadastradas foram: ", end='')
for m in mulheres:
    print(m, end=' ')
print()
print("D) As pessoas que são mais velhas que a média de idade são:")
for i in range(0, len(pam)):
    if i != 0 and i % 2 != 0:
        print(f"{pam[i]} anos")
    else:
        print(f"    {pam[i]}, com ", end='')
print("<< ENCERRADO >>")
