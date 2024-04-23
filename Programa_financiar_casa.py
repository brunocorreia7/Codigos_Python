casa = float(input('valor da casa: R$ '))
salário = float(input('sálario do comprador: R$ '))
anos = int(input('quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print(f'para pagar uma casa de R${casa:.2f}em {anos}anos')
print(f'a prestação será de R${prestação:.2f}')
if prestação <=mínimo:
    print('emprestimo pode ser concedido!')
else:
    print('emprestimo negado!')