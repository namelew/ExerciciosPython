#mostrar categoria atleta
#até 9 anos = mirim
#até 14 anos = infantil
#até 19 anos = sênior
#de 20 anos para frente = master
from datetime import date
at = date.today().year
an = int(input("Digite o ano de nascimento: "))
i = at - an
if i <= 9:
    print("Categoria Mirim")
elif i <= 14:
    print("Categoria Infantil")
elif i <= 19:
    print("Categoria Junior")
elif i <= 25:
    print("Categoria Sênior")
elif i > 25:
    print("Categoria Master")
else:
    print("\033[1;31mErro! Digite uma idade válida")
