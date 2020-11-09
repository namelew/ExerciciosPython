#ansi de cor
#sintase: \033[style;text;back m
#style: estilo da fonte.
#tipos: 0(sem estilo"none"), 1(Negrito"Bold"), 4(Sublinado"Underline"), 7(Inverte configurações"Negative").
#text: cor do texto, vai de 30-37.
#tipos: 30(white),31(red),32(green),33(yellow),34(blue),35(purple),36(ciano),37(grey).
#back:cor do  fundo do terminal.
#tipos:mesmas cores, mas de 40-47.
#p.s: existem outros tipos, mas esses são os básicos.
nome = "Diogo"
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pb': '\33[7;30m'}
print(f"Olá, muito prazer em te conhecer,{cores['pb']} { nome} {cores['limpa']}!!")
