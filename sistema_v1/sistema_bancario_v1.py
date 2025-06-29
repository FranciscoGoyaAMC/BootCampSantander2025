def mostrar_menu():
    print("MENU PRINCIPAL\n[1] - Depositar\n[2] - Sacar\n[3] - Extrato\n[0] - Sair")

def depositar(saldo, extrato):
    try:
        valor = float(input("Digite o valor de depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\nDepósito realizado com sucesso.")
        else:
            print("\nValor inválido. O depósito deve ser positivo.")
    except ValueError:
        print("\nOperação falhou. Valor inválido.")
    return saldo, extrato

def sacar(saldo, extrato, numero_saques):
    try:
        valor = float(input("Digite o valor de saque: "))
        if valor <= 0:
            print("\nValor inválido. O saque deve ser positivo.")
        elif valor > saldo:
            print("\nSaldo insuficiente para saque.")
        elif numero_saques >= LIMITE_SAQUES:
            print("\nNúmero máximo de saques diários atingido.")
        elif valor > LIMITE_TRANSACAO:
            print(f"\nValor do saque excede o limite de R$ {LIMITE_TRANSACAO:.2f}.")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("\nSaque realizado com sucesso.")
    except ValueError:
        print("\nOperação falhou. Valor inválido.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# Código principal
saldo = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
LIMITE_TRANSACAO = 500

while True:
    mostrar_menu()
    try:
        opcao = int(input("\nDigite a opção desejada: "))
    except ValueError:
        print("\nOpção inválida. Digite um número entre 0 e 3.")
        continue

    if opcao == 1:
        print("\nSelecionado: Depósito\n")
        saldo, extrato = depositar(saldo, extrato)
    elif opcao == 2:
        print("\nSelecionado: Saque\n")
        saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques)
    elif opcao == 3:
        print("\nSelecionado: Extrato\n")
        exibir_extrato(saldo, extrato)
    elif opcao == 0:
        print("\nFinalizando o sistema")
        break
    else:
        print("\nOpção inválida. Digite um número entre 0 e 3.")
