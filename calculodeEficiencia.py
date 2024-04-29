hora_reportada = float(input('Digite horas reportadas: '))
hora_rh = float(input('Digite horas do RH: '))
eficiencia = hora_reportada / hora_rh
print(f'A eficiência foi {eficiencia:.2%}')

if eficiencia >= 0.80:
    print('Parabens! Você conseguiu uma boa eficiência.')
elif 0.50 <= eficiencia <= 0.79:
    print('Você precisa melhorar um pouco a eficiência.')
else:
    print('A eficiencia foi ruim')

