import menu
from Ferramentas import String, Dados
from time import sleep as slp
arq = 'agenda.txt'
if not menu.arquivoExiste(arq):
    menu.criar(arq)
while True:
    String.titulo("MENU PRINCIPAL", c=6, tan=42)
    resposta = menu.menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do Sistema"])
    if resposta == 1:
        String.titulo('OPÇÃO 1', c=6, tan=42)
        menu.mostrarArquivo(arq)
    elif resposta == 2:
        String.titulo('OPÇÃO 2',  c=6, tan=42)
        String.titulo("NOVO CADASTRO", c=6, tan=42)
        nome = input("Nome: ")
        idade = Dados.leiaInt("Idade: ")
        menu.cadastra(arq, nome, idade)
    elif resposta == 3:
        break
    else:
        print("\033[0;31mOpção inválida! Por favor, digite uma das opções acima.\033[m")
    slp(2)
String.titulo("VOLTE SEMPRE", c=6, tan=42)
