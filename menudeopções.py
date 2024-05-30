
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

menu = """
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa
=> """

while True:
    opcao = input(menu)
    
    if opcao == '1':
        soma = n1 + n2
        print(f'A soma é {soma}')
        
    elif opcao == '2':
        multiplicacao = n1 * n2
        print(f'A multiplicação é {multiplicacao}')
        
    elif opcao == '3':
        maior = max(n1, n2)
        print(f'O maior número é {maior}')
        
    elif opcao == '4':
        n1 = float(input('Digite o novo primeiro valor: '))
        n2 = float(input('Digite o novo segundo valor: '))
        
    elif opcao == '5':
        print('Saindo do programa...')
        break
        
    else:
        print('Opção inválida! Tente novamente.')

