def notas(*n, sit=False):
    s = ma = me = 0
    rel = {}
    rel['total'] = len(n)
    for i in range(0, len(n)):
        if i == 0:
            ma = n[i]
            me = n[i]
        else:
            if n[i] > ma:
                ma = n[i]
            if n[i] < me:
                me = n[i]
        s += n[i]
    rel['maior'] = ma
    rel['menor'] = me
    rel['media'] = s/len(n)
    if sit:
        if rel['media'] > 8:
            rel['situação'] = 'Muito Boa'
        elif 7 < rel['media'] <= 8:
            rel['situação'] = 'Boa'
        elif 6 < rel['media'] <= 7:
            rel['situação'] = 'Mediana'
        elif 4 < rel['media'] <= 6:
            rel['situação'] = 'Ruim'
        else:
            rel['situação'] = 'Muito Ruim'
    return rel


resp = notas(9.55, 9.5, 9.5, sit=True)
print(resp)
