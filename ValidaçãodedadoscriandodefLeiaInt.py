def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro! digite um número inteiro valido.\033[m')
        if ok:
            break 
    return valor
    
# programa principal
n = leiaInt('Digite um número: ')
print(f'você acabou de digitar o número {n}')