n = input('Insira algo ')
cores = {"limpa": '\033[m', "yellow": '\033[33m', "roxo": '\033[35m', 'ciano': '\033[36m',
         "verde": '\033[32m'}
print(f'{cores["yellow"]}Tipo da Variável= {type(n)}')
print(f'{cores["roxo"]}É um número? { n.isnumeric()}')
print(f'{cores["roxo"]}É letra? {n.isalpha()}')
print(f'{cores["roxo"]}É alpha numérico? {n.isalnum()}')
print(f'{cores["roxo"]}É decimal? { n.isdecimal()}')
print(f'{cores["ciano"]}Está em branco? {n.isspace()}')
print(f'{cores["ciano"]}É um digito? {n.isdigit()}')
print(f'{cores["verde"]}Está em maiúsculo? {n.isupper()}')
print(f'{cores["verde"]}Está em minúsculo? {n.islower()}')
print(f'{cores["verde"]}Está capitalizado? {n.istitle()}')
