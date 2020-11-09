# Como criar e modificar arquivos
valores_celulares = [850, 2230, 1500, 3500, 5000]
"""

'r'  -> 'Usado somente para ler algo'
'w'  -> 'Usado somente para escrever algo'
'r+' -> 'Usado para ler e escrever algo'
'a'  -> 'Usado para acrescentar algo'

"""
# O 'w' sempre sobrescrever os arquivos
# with open('valores_celulares.txt', 'w') as arquivo:
#    for valor in valores_celulares:
#        arquivo.write(str(valor) + '\n')
# O 'a' acrescenta sem sobrescrever
# with open('valores_celulares.txt', 'a') as arquivo:
#    for valor in valores_celulares:
#        arquivo.write(str(valor) + '\n')
# O 'r' apenas lê sem alterar nada
# with open('valores_celulares.txt', 'r') as arquivo:
#    for valor in arquivo:
#        print(valor)
with open('valores_celulares.txt', 'r+') as arquivo:
    for valor in arquivo:
        print(valor)
    arquivo.write("\n9000")
