# código baseado no post *Gerando senhas aleatórios com python*
# da página do instagram @divers_tech 
from random import sample
from string import ascii_letters

letras = ascii_letters
numeros = '0123456789'
special_caracters = "-+*%&!_"

total = letras + numeros + special_caracters
tamanho = int(input("Tamanho da senha: "))

senha = ''.join(sample(total, tamanho))
print(senha) 