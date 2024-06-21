limite = 600
limiteDeposito = 1000
saldo = 1000
limiteSaque = 2

welcome = "Seja bem vindo(a) ao LBank"
print(welcome.center(80, "#"))
print("")
while True:
    try:
        opcao = int(input("Selecione qual opção deseja: [1] saque [2] Extrato [3] Depósito: ")) 
        if opcao == 1:

            numeroSaque = 1

            while True:

                user_input = input("Digite o valor a sacar: ")
                
                if user_input.lower() in ["exit", "quit"]:
                    print("Saindo...")
                    break
                try:
                
                    valor = float(user_input)

                    if valor > limite:
                        print(f"Seu limite de saque é: R${limite: .2f}")
                    elif valor > saldo:
                        print("Saldo Insuficiente")
                        break
                    elif numeroSaque > limiteSaque:
                        print("Limite de saque atingido")
                        break
                    else:
                        saldo -= valor
                        print(f"seu saque foi concluído. Seu novo saldo é: R${saldo: .2f}")
                        numeroSaque += 1
                        while True:
                            new_input = input(f"Gostaria de fazer outro saque? [1]Sim  [2]Não: ")
                            try:
                                new_input = int(new_input)
                                if new_input == 1:
                                    break
                                elif new_input == 2:
                                    print("Obrigado por utilizar nossos serviços, volte sempre!")
                                    exit()
                                else:
                                    print("Digite uma opção válida")
                            except ValueError:
                                print("Erro: Insíra um número válido")
                except ValueError:
                    print("Erro: Insíra um número válido")

        elif opcao == 2:
            print("exibindo o extrato:...")
            print(f"Seu saldo é: R${saldo: .2f} ")    
            print("Muito obrigado por utilizar nossos serviços, volte sempre!")

        elif opcao == 3:
            while True:
                deposito_input = input("Digite o valor a depositar: ")
                
                if deposito_input.lower() in ["exit", "quit"]:
                    print("Saindo...")
                    break
                try:
                    
                    valor = float(deposito_input)

                    if valor > limiteDeposito:
                        print(f"Seu limite de depósito é: R${limiteDeposito: .2f}")
                    else:
                        saldo += valor
                        print(f"seu depósito foi concluído. Seu novo saldo é: R${saldo: .2f}")
                        while True:
                            newer_input = input(f"Gostaria de fazer outro depósito? [1]Sim  [2]Não: ")
                            try:
                                newer_input = int(newer_input)
                                if newer_input == 1:
                                    break
                                elif newer_input == 2:
                                    print("Obrigado por utilizar nossos serviços, volte sempre!")
                                    exit()
                                else:
                                    print("Digite uma opção válida")
                            except ValueError:
                                print("Erro: Insíra um número válido")
                except ValueError:
                    print("Erro: Insíra um número válido") 
        else:
            print("digite uma opção válida")
    except ValueError:
        print("Erro: Insira um número válido")
