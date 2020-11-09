#Dizer se um carro ultrapassou ou não o limite de 80 km/h
#Se sim, dizer que foi multado e dar o valor da multa
#Multa = R$ 7,00 * Cada Km/h acima do limite
print("-"*20,"Medidor de Velocidade","-"*20)
v = float(input("Digite a velocidade do veículo\n"))
if v<=80:
    print("Está dentro do limite de velocidade da via. Tenha um bom dia")
else:
    print(f"O veículo está acima do limite permitido e deverá pagar uma multa de R$ {(v-80)*7:.2f}")
