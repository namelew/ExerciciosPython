def contador(x, y, z):
    print(f"Contagem de {x} até {y} de {abs(z)} em {abs(z)}")
    sleep(1.5)
    for i in range(x, y+1, z):
        print(i, end=' ', flush=False)
        sleep(0.5)
    print("FIM!")
def lr():
    print("-=" * 30)
def l():
    print("-" * 40)


from time import sleep
lr()
sleep(1)
contador(1, 10, 1)
sleep(1)
l()
sleep(1)
contador(10, 0, -2)
sleep(1)
l()
sleep(1)
print("Contagem personalizada! Agora é a sua vez")
sleep(1)
contador(int(input("Início: ")), int(input("Fim: ")), int(input("Passo: ")))
sleep(1)
lr()
