def mostrar_menu():
    print("MENU PRINCIPAL\n[1] - Depositar\n[2] - Sacar\n[3] - Extrato\n[4] - Criar Usuário\n[5] - Criar Conta Corrente\n[0] - Sair")


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\nDepósito realizado com sucesso.")
    else:
        print("\nValor inválido. O depósito deve ser positivo.")

    return saldo, extrato


def sacar(*,saldo, valor, extrato, limite_transacao,numero_saques, limite_saques):
    if valor <= 0:
        print("\nValor inválido. O saque deve ser positivo.")
    elif valor > saldo:
        print("\nSaldo insuficiente para saque.")
    elif numero_saques >= limite_saques:
            print("\nNúmero máximo de saques diários atingido.")
    elif valor > limite_transacao:
        print(f"\nValor do saque excede o limite de R$ {limite_transacao:.2f}.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\nSaque realizado com sucesso.")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def buscar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None


def criar_usuario(usuarios):
    cpf = input("Digite o CPF do usuário (somente números): ").strip()
    if not cpf.isdigit():
        print("\nCPF inválido. Deve conter apenas números.")
        return
    usuario = buscar_usuario(cpf, usuarios)

    if usuario:
        print("\nUsuário já cadastrado.")
        return
    
    nome = input("Digite o nome completo do usuário: ").upper()
    data_nascimento = input("Digite a data de nascimento do usuário (DD/MM/AAAA): ").strip()
    endereco = input("Digite o endereço do usuário (rua, número - bairro - cidade/UF): ")

    usuarios.append({
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    })

    print("\nUsuário cadastrado com sucesso!")




def criar_conta_corrente(agencia, numero_conta, usuarios):
    try:
        cpf = int(input("Digite o CPF do usuário (somente números): "))
    except ValueError:
        print("\nCPF inválido. Deve conter apenas números.")
        return
    usuario = buscar_usuario(cpf, usuarios)

    if usuario:
        return {"agencia": agencia,
                "numero_conta": numero_conta,
                "usuario": usuario}
    
    print("\nUsuário não encontrado.")
    return None


def main():
    LIMITE_SAQUES = 3
    LIMITE_TRANSACAO = 500
    AGENCIA = "0001"

    saldo = 0
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        mostrar_menu()
        try:
            opcao = int(input("\nDigite a opção desejada: "))
        except ValueError:
            print("\nOpção inválida. Digite um número entre 0 e 5.")
            continue

        if opcao == 1:
            print("\nSelecionado: Depósito\n")
            try:
                valor = float(input("Digite o valor de depósito: "))
                saldo, extrato = depositar(saldo, valor, extrato)
            except ValueError:
                print("\nOperação falhou. Valor inválido.")

        elif opcao == 2:
            print("\nSelecionado: Saque\n")
            try:
                valor = float(input("Digite o valor de saque: "))
                saldo, extrato, numero_saques = sacar(saldo=saldo,
                                                      valor=valor,
                                                      extrato=extrato,
                                                      limite_transacao=LIMITE_TRANSACAO,
                                                      numero_saques=numero_saques,
                                                      limite_saques=LIMITE_SAQUES)
            except ValueError:
                print("\nOperação falhou. Valor inválido.")

        elif opcao == 3:
            print("\nSelecionado: Extrato\n")
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 4:
            print("\nSelecionado: Criar Usuário\n")
            criar_usuario(usuarios)

        elif opcao == 5:
            print("\nSelecionado: Criar Conta Corrente\n")
            numero_conta = len(contas) + 1
            conta = criar_conta_corrente(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                print(f"\nConta criada com sucesso! Número da conta: {numero_conta}, Agência: {AGENCIA}")

        elif opcao == 0:
            print("\nFinalizando o sistema")
            break

        else:
            print("\nOpção inválida. Digite um número entre 0 e 5.")


main()
