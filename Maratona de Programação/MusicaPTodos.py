gosto = []
#entrada
conta = input().split(' ')
for n in range(0, int(conta[0])):
    user = input().split(' ')
    gosto.append(user)
#processamento
play = int(conta[2])
trocas = c = ci = 0
while True:
    while True:
        ci += 1
        if ci == 2:
            break
        if play == int(gosto[c][1]):
            play = int(gosto[c][0])
            trocas += 1
            if trocas > len(gosto):
                trocas = -1
                play = -1
                break
            c += 1
            continue
        c = 0
    if play >= int(conta[1]) or play == -1:
        break
#saida
print(trocas)
