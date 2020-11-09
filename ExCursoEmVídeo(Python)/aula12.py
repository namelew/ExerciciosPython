nome = str(input("Qual o seu nome? "))
if nome == "Diogo":
    print("Seu nome é muito bonito")
elif nome == "Ana" or nome == "Maria" or nome == "João":
    print("Seu nome é bem popular no Brasil")
elif nome in "Cláudia Juliana Jéssica Ana":
    print("Que belo nome feminino")
else:
    print("Seu nome é bem normal")
print("Tenha um bom dia,", nome)
