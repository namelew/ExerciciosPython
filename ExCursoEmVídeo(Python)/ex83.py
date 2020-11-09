e = str(input("Expressão: "))
l = []
for v in e:
    if v == '(':
        l.append('(')
    else:
        if len(l) > 0:
            l.pop()
        else:
            l.append('(')
        break
if len(l) == 0:
    print("Expressão válida")
else:
    print("Expressão inválida")
