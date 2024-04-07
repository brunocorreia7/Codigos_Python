velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade >80:
    print('\033[31mvocê foi multado! Você excedeu o limite permitido que é de 80km/h')
    multa = (velocidade-80) * 7 
    print(f'você deve pagar uma multa de {multa:.2f}R$')
else:
    print('você está na velocidade permitida.')
