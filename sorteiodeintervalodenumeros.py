import random

while True:
    try:
        inicio = int(input('Digite o valor inicial do intervalo: '))
        fim = int(input('Digite o valor final do intervalo: '))
        break
    except:
        print("Erro! digite um número inteiro válido.")


lista = list(range(inicio, fim+1))


escolhido = random.choice(lista)

print(f'O número escolhido foi {escolhido}')
