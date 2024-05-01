peso = float(input('Digite o seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura ** 2)

print(f'Sua altura é {altura:.2f}m e seu peso é {peso}kg.')
print(f'Sendo assim, o seu IMC é {imc:.2f}.')

if imc < 18.5:
    print('Abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Peso normal.')
elif 25 <= imc < 30:
    print('Sobrepeso.')
else:
    print('Obeso.')


