#cálculo IMC
#Tabela:
#imc < 18.5 == "Abaixo do Peso"
#18.5 <= imc < 25 == "Peso Ideal"
#25 <= imc < 30 == "Sobrepeso"
#30 <= imc < 40 == "Obesidade"
#imc >= 40 == "Obesidade Morbida"
p = float(input("Insira o se peso, em KG\n"))
a = float(input("Insira sua altura, em metros\n"))
imc = p/a**2
if a <= 0 or p <= 0:
    print("\033[1;31mErro!Digite valores válidos")
elif imc < 18.5:
    print("\033[1;31mAbaixo do peso")
elif 18.5 <= imc < 25:
    print("\033[1;34mPeso ideal")
elif 25 <= imc < 30:
    print("\033[31mSobrepeso")
elif 30 <= imc < 40:
    print("\033[7mObesidade\033[0m")
elif imc >= 40:
    print("\033[7;31mObesidade Morbida\033[0m")
