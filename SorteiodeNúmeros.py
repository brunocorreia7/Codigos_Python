import random
lista = []
for c in range(0, 4):
    n = int(input('digite um número '))
    lista.append(n)
escolhido = random.choice(lista)
print(f'o número sorteado foi {escolhido}')



