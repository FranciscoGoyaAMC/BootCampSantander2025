from abc import ABC, abstractmethod
from datetime import datetime
import re


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []


    def realizar_transacao(self, conta, transacao):
       transacao.registrar(conta)
    

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)


    @property
    def saldo(self):
        return self._saldo
    

    @property
    def numero(self):
        return self._numero
    

    @property
    def agencia(self):
        return self._agencia
    

    @property
    def cliente(self):
        return self._cliente
    

    @property
    def historico(self):
        return self._historico


    def sacar(self, valor):
        saldo = self.saldo
        excedeu = valor > saldo
        
        if excedeu:
            print("Erro: Saldo insuficiente para realizar o saque.")
            return False
        
        if valor > 0:
            self._saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
            return True
        
        print("Erro: Valor informado é inválido.")
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
            return True
        
        print("Erro: Valor informado é inválido.")
        return False
    

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite_por_transacao=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite_por_transacao = limite_por_transacao
        self.limite_saques = limite_saques
    

    def sacar(self, valor) -> bool:
        numero_saques = len([transacao for transacao in self.historico.obter_transacoes if transacao["tipo"] == Saque.__name__])
        excedeu_transacao = valor > self.limite_por_transacao
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_saques:
            print("Erro: Limite de saques atingido.")

        if excedeu_transacao:
            print("Erro: Limite por transação excedido.")

        else:
            return super().sacar(valor)
        
        return False
    

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def obter_transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass
    
    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        transacao_ok = conta.sacar(self.valor)

        if transacao_ok:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor: float):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        transacao_ok = conta.depositar(self.valor)

        if transacao_ok:
            conta.historico.adicionar_transacao(self)


class Validador:
    def validar_cpf(self, cpf):
        return re.fullmatch(r"\d{11}", cpf) is not None

    def validar_nascimento(self, data_nascimento):
        if re.fullmatch(r"\d{2}/\d{2}/\d{4}", data_nascimento):
            try:
                datetime.strptime(data_nascimento, "%d/%m/%Y")
                return True
            except ValueError:
                return False
        return False

    def validar_endereco(self, endereco):
        padrao = r"^[\w\s\.\-À-ÿ]+,\s*\d+\s*-\s*[\w\sÀ-ÿ]+-\s*[\w\sÀ-ÿ]+\/[A-Z]{2}$"
        return re.fullmatch(padrao, endereco.strip()) is not None
    

class Filtros:
    def filtrar_clientes(self, cpf, clientes):
        clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
        return clientes_filtrados[0] if clientes_filtrados else None
    
    def filtrar_conta(self, clientes):
        if not clientes.contas:
            return None
        return clientes.contas[0]
    

class Operacoes:
    validador = Validador()
    filtros = Filtros()

    def criar_cliente(self, clientes):
        cpf = input("Digite seu CPF (somente números): ")
        cpf_valido = self.validador.validar_cpf(cpf)
        while not cpf_valido:
            print("Digite um cpf válido")
            cpf = input("Digite seu CPF (somente números): ")
            cpf_valido = self.validador.validar_cpf(cpf)

        cliente = self.filtros.filtrar_clientes(cpf, clientes)

        if not cliente:
            nome = input("Digite seu nome completo: ").upper().strip()
            data_nascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ")
            data_valida = self.validador.validar_nascimento(data_nascimento)
            while not data_valida:
                print("Digite uma data válida")
                data_nascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ")
                data_valida = self.validador.validar_nascimento(data_nascimento)

            endereco = input("Digite seu endereço no formato (Rua, Número - Bairro - Cidade/UF): ").upper().strip()
            endereco_valido = self.validador.validar_endereco(endereco)
            while not endereco_valido:
                print("Digite um endereço válido")
                endereco = input("Digite seu endereço no formato (Rua, Número - Bairro - Cidade/UF): ").upper().strip()
                endereco_valido = self.validador.validar_endereco(endereco)

            cliente = PessoaFisica(nome=nome, cpf=cpf, data_nascimento=data_nascimento, endereco=endereco)
            clientes.append(cliente)
            print(f"Usuário {cliente.nome} criado com sucesso!")
            return

        else:
            print(f"Usuário {cliente.nome} já existe.")
            return

        
    def criar_conta(self, numero_conta, clientes, contas):
        cpf = input("Digite o CPF do cliente (somente números): ")
        cpf_valido = self.validador.validar_cpf(cpf)
        while not cpf_valido:
            print("Digite um cpf válido")
            cpf = input("Digite o CPF (somente números): ")
            cpf_valido = self.validador.validar_cpf(cpf)
        cliente = self.filtros.filtrar_clientes(cpf, clientes)
        if not cliente:
            print("Erro: Cliente não encontrado.")
            return

        conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
        contas.append(conta)
        cliente.contas.append(conta)
        print(f"Conta {conta.numero} criada com sucesso!")
        return
    
    def deposito(self, clientes):
        cpf = input("Digite o CPF do cliente (somente números): ")
        cpf_valido = self.validador.validar_cpf(cpf)
        while not cpf_valido:
            print("Digite um cpf válido")
            cpf = input("Digite o CPF (somente números): ")
            cpf_valido = self.validador.validar_cpf(cpf)
        
        cliente = self.filtros.filtrar_clientes(cpf, clientes)
        if not cliente:
            print("Erro: Cliente não encontrado.")
            return
        
        conta = self.filtros.filtrar_conta(cliente)
        if not conta:
            print("Erro: Conta não encontrada.")
            return

        try:
            valor = float(input("Digite o valor da operação: "))
        except ValueError:
            print("Valor inválido. Por favor, insira um número.")
            return
                    
        transacao = Deposito(valor)
        cliente.realizar_transacao(conta, transacao)
        return
    
    def saque(self, clientes):
        cpf = input("Digite o CPF do cliente (somente números): ")
        cpf_valido = self.validador.validar_cpf(cpf)
        while not cpf_valido:
            print("Digite um cpf válido")
            cpf = input("Digite o CPF (somente números): ")
            cpf_valido = self.validador.validar_cpf(cpf)
        
        cliente = self.filtros.filtrar_clientes(cpf, clientes)
        if not cliente:
            print("Erro: Cliente não encontrado.")
            return
        
        conta = self.filtros.filtrar_conta(cliente)
        if not cliente:
            print("Erro: Cliente não encontrado.")
            return
                
        conta = self.filtros.filtrar_conta(cliente)
        if not conta:
            print("Erro: Conta não encontrada.")
            return
                
        try:
            valor = float(input("Digite o valor da operação: "))
        except ValueError:
            print("Valor inválido. Por favor, insira um número.")
            return

        transacao = Saque(valor)
        cliente.realizar_transacao(conta, transacao)
        return
    
    def extrato(self, clientes):
        cpf = input("Digite o CPF do cliente (somente números): ")
        cpf_valido = self.validador.validar_cpf(cpf)
        while not cpf_valido:
            print("Digite um cpf válido")
            cpf = input("Digite o CPF (somente números): ")
            cpf_valido = self.validador.validar_cpf(cpf)
        
        cliente = self.filtros.filtrar_clientes(cpf, clientes)
        if not cliente:
            print("Erro: Cliente não encontrado.")
            return
        
        conta = self.filtros.filtrar_conta(cliente)
        if not cliente:
            print("Erro: Cliente não encontrado.")
            return

        conta = self.filtros.filtrar_conta(cliente)
        if not conta:
            print("Erro: Conta não encontrada.")
            return
        
        print("EXTRATO")
        transacoes = conta.historico.obter_transacoes
        extrato = ""
        
        if not transacoes:
            print("Nenhuma transação encontrada.")
            return         
       
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR${transacao['valor']:.2f}\n\tData: {transacao['data']}\n"
                    
        print(extrato)
        print(f"\nSaldo:\n\t{conta.saldo:.2f}")
        print("-" * 20)
        return
        

class Menu:
    def __init__(self):
        self.opcoes = {
            1: "Criar Usuário",
            2: "Criar Conta",
            3: "Depositar",
            4: "Sacar",
            5: "Extrato",
            6: "Sair"
        }

    def exibir_menu(self):
        print("\nMENU PRINCIPAL:")
        for key, value in self.opcoes.items():
            print(f"{key} - {value}")

    def obter_opcao(self):
        while True:
            try:
                opcao = int(input("Escolha uma opção: "))
                if opcao in self.opcoes:
                    return opcao
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número de 1 a 6.")


def main():
    clientes = []
    contas = []
    
    menu = Menu()
    menu.exibir_menu()
    operacao = Operacoes()
    opcao = menu.obter_opcao()

    while True:
        if opcao == 1:
            operacao.criar_cliente(clientes)
            menu.exibir_menu()
            opcao = menu.obter_opcao()
        if opcao == 2:
            numero = len(contas) + 1
            operacao.criar_conta(numero, clientes, contas)
            menu.exibir_menu()
            opcao = menu.obter_opcao()
        if opcao == 3:
            operacao.deposito(clientes)
            menu.exibir_menu()
            opcao = menu.obter_opcao()
        if opcao == 4:
            operacao.saque(clientes)
            menu.exibir_menu()
            opcao = menu.obter_opcao()
        if opcao == 5:
            operacao.extrato(clientes)
            menu.exibir_menu()
            opcao = menu.obter_opcao()
        if opcao == 6:
            print("FECHANDO SISTEMA")
            break

main()
