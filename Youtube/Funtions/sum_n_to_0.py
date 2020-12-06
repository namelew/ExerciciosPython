# Exercúcio
# Função que retorna a soma de n até 0

def soma_decrescente(n):
    if n == 0:
        return n
    return soma_decrescente(n-1) + n

print(soma_decrescente(5))