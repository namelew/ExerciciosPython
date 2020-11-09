frase = ' Curso em Vídeo Python '
# [] = indicador de lista
# x : y = fatiamento de frase, onde x demarca início e y fim
# caso x  : y, onde y = 0, ele considerará de X ao fim da string
# x : y : z = fatiamento, onde z equivale a espaços ignorados
# len = quantidade de sub-espaços em uma frase
# x.count('') = mostra a quantidade de vezes que '' apareceu na string
# x.count('', x, y) = demarca range da busca, onde x é o início e y é o final. Contasse y-1
# x.find('') = encontra '', caso mais de 1 caractere, mostra o início de ''
# # x.find('') = -1 = "-1" significa que '' não existe na string
# # '' in x = retorna se '' existe ou não na string
# frase.replace('', '') = substitui o valor em '' pelo valor em ''. Substitui de forma secundária
# frase.upper() = transforma todas as letras em minusculo para maiúculo, mantendo as que já estava em maiúsculo
# frase.lower() = o contrário do ".upper"
# frase.capitalize() = joga todos os outros caracteres para minúsculo, mantendo/mudando o primeiro para maiúsculo
# frase.title() = transforma todos as primeiras letras de cada palavra em maiúsculo, deixando o resto minúsculo
# frase.strip() = romove todos os espaços inúteis no inicio e no final da string
# frase.rstrip() = remove somente os espaços no final da string
# frase.lstrip() = remove apenas os espaços no inicio da string
# frase.split() = gera uma lista com todas as palavras de ua lista de caracteres
# ''.join = junta palavras e pode usar o '' como separador
print(frase[9::2])
print(len(frase))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())
print(frase.split())
print('-'.join(frase.split()))
