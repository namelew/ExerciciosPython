#input
#ano de nascimento
#processamento
#calcular a idade e ver se ele pode ou não se alistar
#output
#dizer se ele deve se alistar, não tem idade suficiente ou ja passou do tempo de se alistar
#mostrar também o tempo que falta pra se alistar ou quanto ja passou
from datetime import date
s = input("Qual o seu sexo?(M: Masc., F: Femin.) ")
if s == "F":
    print("Você não precisa se alistar")
else:
    at = date.today().year
    an = int(input("Digite se ano de nascimento: "))
    i = at - an
    if 18 <= i < 45:
        print("\033[1;32mVc deve se alistar")
        if i > 18:
            print(f"\033[1;31mVoce passou {i-18} anos da idade de se alistar.", end='')
            print(f" Seu alistamento deveria ter sido em {at-(i-18)}")
            print("Apresentesse a Junta Militar mais próxima")
        elif i < 18:
            print("\033[34mVc não possui idade suficiente para se alistar. ", end="")
            print(f"Faltam \033[1;35m{18-i}\033[0;34m anos e seu alistamento será em {(18-i)+an}")
        elif i >= 45:
            print("Você completou os seus 27 anos de reservista e não precisa mais servir")