try:
    #o inicio de um sonho
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a/b
except KeyboardInterrupt:
    print("O usuário preferiu não informar os valores.")
except (ValueError, TypeError):
    #deu tudo errado
    print("Tivemos um problema com os tipos de dados que você digitou.")
except ZeroDivisionError:
    print("Não é possivel dividir um número por 0.")
except Exception as erro:
    print(f"O erro encontrado foi {erro.__cause__}")
else:
    #deu tudo certo
    print(r)
finally:
    #acordei
    print("Volte Sempre! Muito Obrigado")
