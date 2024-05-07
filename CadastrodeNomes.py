menu = """
[c] cadastrar
[m] mostrar cadastrados
[s] sair

= > """
cadastro = []

while True:
    opcao = input(menu)
    if opcao == "c":
        nome = input('Digite o nome da pessoa: ')
        cadastro.append(nome)
    elif opcao == "m":
        print("Pessoas cadastradas:", cadastro)
    elif opcao == "s":
        print('Obrigado por usar o programa.')
        break
