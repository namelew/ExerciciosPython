n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'A soma vale {s},\nO produto vale {m},\nO quoiciente vale {d:.3f},', end=' ')
print(f'a divisão inteira vale {di} e a potência vale {e}')
