# Sistema Bancário em Python

Este é um projeto simples de sistema bancário desenvolvido em Python como parte de um desafio do **Bootcamp Santander Backend com Python**, promovido pela **DIO (Digital Innovation One)** em parceria com a **Santander Open Academy**.

## Descrição

O sistema simula operações bancárias básicas, permitindo que o usuário interaja com um menu para:

* Depositar valores
* Sacar valores (respeitando limites)
* Visualizar o extrato bancário
* Encerrar o programa

Todos os dados são armazenados temporariamente durante a execução do programa, sem persistência em arquivos ou bancos de dados.

## Funcionalidades

* **Depósito**: Permite apenas valores positivos. O valor é somado ao saldo e registrado no extrato.
* **Saque**: Permite saques até R\$500, respeitando um limite de 3 saques por execução e apenas se houver saldo suficiente.
* **Extrato**: Mostra todas as movimentações realizadas e o saldo atual.

## Requisitos

* Python 3.7 ou superior

## Como executar

1. Clone o repositório ou copie o arquivo `sistema_bancario.py` para seu computador.
2. Execute o arquivo:

```bash
python sistema_bancario.py
```

3. Siga as instruções exibidas no terminal.

## Exemplo de uso

```
MENU PRINCIPAL
[1] - Depositar
[2] - Sacar
[3] - Extrato
[0] - Sair

Digite a opção desejada: 1
Selecionado: Depósito
Digite o valor de depósito: 200
Depósito realizado com sucesso.
```

## Autor

Francisco Goya
Estudante de Análise e Desenvolvimento de Sistemas
Bootcamp Santander Backend com Python - DIO/Santander Open Academy

## Licença

Este projeto está licenciado sob a Licença MIT.
