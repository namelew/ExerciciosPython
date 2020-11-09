#ler a distânia em Km de uma viagem e calcular o preço da passagem
#Distância <= 200 km, passagem de R$ 0,50 por quilômetro
#Distância >200 km,passagem de R$ 0,45 po km
print('-'*20, "Passagem de Ônibus", '-'*20)
d = int(input("Quantos quilômetros deseja viajar?\n"))
preço = d * 0.50 if d <= 200 else d * 0.45
print(f"Viajando {d} km, sua passagem custará R$ {preço:.2f}.")
#if d<= 200:
    #print(f"Viajando {d} km, sua passagem custará R$ {d*0.50:.2f}.")
#else:
    #print(f"Viajando {d} km, sua passagem custará R$ {d*0.45:.2f}.")
