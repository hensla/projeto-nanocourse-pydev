opcao = 0





while opcao != 3:
    print("1 - Receber um elogio")
    print("2 - Calcular o fatorial de um número")
    print("3 - Sair")
    opcao = int(input("Informe o número da opção desejada e depois tecle ENTER: "))
    if opcao == 1:
        print("Você é uma pessoa muito esperta")
    elif opcao == 2:
        numero = int(input("Informe um número do qual deseja o fatorial: "))
        fat = numero

        for valor in range(1, numero, 1):
            fat = fat * valor

        print(f"O fatorial para o valor informado foi {fat}.")

    elif opcao == 3:
        print("Saindo do sistema...")

    else:
        print("Digite uma opção válida.")