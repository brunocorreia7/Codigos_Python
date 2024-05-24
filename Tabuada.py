while True:
    try:
        numero = int(input('Digite um número inteiro para ver sua tabuada: '))
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro válido.")

for c in range(1, 11):
    print(f'{numero} X {c} = {numero * c}')
