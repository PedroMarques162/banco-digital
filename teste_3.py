menu = """ 
[0] Sair
[1] Extrato
[2] Sacar
[3] Depositar

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "3":
        valor = float(input("Informe o valor do depósito:R$ "))
        
        if valor <= 0:
            print("\n❌ Operação falhou! O valor informado é inválido.")
        else:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n" 
            print("\n✅ Depósito realizado com sucesso!")
        
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        
        if valor <= 0:
            print("\n❌ Operação falhou! O valor informado é inválido.")
        elif valor > saldo:
            print("\n❌ Operação falhou! Você não tem saldo suficiente.")
        elif valor > limite:
            print("\n❌ Operação falhou! O valor do saque excede o limite de R$ 500,00.")
        elif numero_saques >= LIMITE_SAQUES:
            print("\n❌ Operação falhou! Número máximo de saques diários atingido.")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("\n✅ Saque realizado com sucesso!")
    
    elif opcao == "1":
        print("\n================ EXTRATO ================")
        print(extrato if extrato else "Nenhuma movimentação registrada.")
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("===========================================")
    
    elif opcao == "0":
        print("\n👋 Obrigado por usar nosso sistema. Até logo!")
        break
    
    else:
        print("\n❌ Operação inválida, por favor selecione uma opção válida.")
