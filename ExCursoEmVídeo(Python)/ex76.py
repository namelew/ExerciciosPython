print("-"*50)
print(f"{'Lista de Preços':^50}")
print("-"*50)
p = ('Lápis', 1.50,
     'Caneta', 2.30,
     'Caderno', 19.99,
     'Estojo', 5.68,
     'Transferidor', 15.45,
     'Mochila', 160.89)
for c in range(0, len(p)):
    if c % 2 == 0:
        print(f'{p[c]:.<40}', end='')
    else:
        print(f'R$ {p[c]:>7.2f}')
print("-"*50)