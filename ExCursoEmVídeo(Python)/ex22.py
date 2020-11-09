nome = str(input("Qual o seu nome?\n")).strip()
div = nome.split()
print(f"Seu nome com todas as letras maiúsculas é {nome.upper()}. Com todas as letras minúsculas é {nome.lower()}.")
print(f"Ele possui {len (''.join(div))} letras. Sendo que, o primeiro nome, possui {len(div[0])} letras.")
