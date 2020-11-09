n = input("Digite uma frase\n").upper().strip()
print(f"Na frase a letra 'A' apareceu {n.count('A')} vezes")
print(f"Ela apareceu pela primeria vez na posição {n.find('A')+1}")
print(f"E apareceu pela última vez na posição {n.rfind('A')+1}")
