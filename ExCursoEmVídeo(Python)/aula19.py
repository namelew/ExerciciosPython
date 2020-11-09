#dados = dict() ou dados = {}
#pessoas = {'nome': "Pedro", 'idade': 25, "sexo": 'M'}
#del pessoas['sexo']
#pessoas['nome'] = 'Leandro'
#pessoas['peso'] = 98.5
#print("O {} tem {} anos".format(pessoas['nome'], pessoas['idade']))
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())
#Monstrando Apenas as Keys:
#for k in pessoas.keys():
#    print(k)
#Mostrando apenas os values:
#for v in pessoas.values():
#    print(v)
#Mostrando tudo(x.itens):
#for k, v in pessoas.items():
#    print(f"{k}: {v}")
estado = dict()
brasil = []
#estado1 = {'uf': 'Amapá', 'sigla': 'AP'}
#estado2 = {'uf': 'Pará', 'sigla': 'PA'}
#brasil.append(estado1)
#brasil.append(estado2)
#print(brasil[0]['uf'])
for i in range(0, 3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla: ')
    brasil.append(estado.copy())
for b in brasil:
    for k, v in b.items():
        print(f'{k}: {v}')