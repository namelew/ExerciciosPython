from Ferramentas.String import *
from time import sleep as slp

def cadastra(a, n='desconhecido', i=0):
    try:
        arq = open(a, 'a')
    except:
        print(f"{cor[2]}Houve um erro durante a execução do arquivo!{cor[0]}")
    else:
        try:
            arq.write(f"{n}; {i}\n")
        except Exception as erro:
            print(f"{cor[2]}Houve um erro de {erro} durante a inscrição dos dados!{cor[0]}")
        else:
            titulo(f"{n.upper()} ADICIONADO AOS REGISTROS", c=5)
            arq.close()


def mostrarArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(f"{cor[2]}Erro ao ler o arquivo.{cor[0]}")
    else:
        titulo("PESSOAS CADASTRADAS", c=6, tan=42)
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f"{dado[0]:<30}{dado[1]:>3} anos")
            slp(1)
    finally:
        a.close()


def menu(list):
    from Ferramentas import String, Dados
    c = 1
    print(String.linha())
    for i in list:
        print(f"\033[0;33m{c} -\033[0;34m {i}\033[m")
        c += 1
    print(String.linha())
    o = Dados.leiaInt("Opção: ")
    return o


def arquivoExiste(x):
    try:
        a = open(x, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar(x):
    try:
        a = open(x, 'wt+')
        a.close()
    except:
        print(f"{cor[2]}Houve um erro na criação do arquivo!{cor[[0]]}")
    else:
        print(f"{cor[4]}Arquivo {a} criado com sucesso!{cor[0]}")
