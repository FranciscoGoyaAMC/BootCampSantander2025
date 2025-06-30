# Sistema Bancário em Python - Versão 2

Este projeto é a **versão 2** do sistema bancário desenvolvido como parte do **Bootcamp Santander Backend com Python 2025**, promovido pela [DIO](https://www.dio.me) em parceria com a **Santander Open Academy**.

## 🔄 Novidades desta versão

Nesta versão, o sistema foi expandido com novos recursos importantes:

* [x] **Criação de usuários** com nome, CPF, data de nascimento e endereço (CPF é único).
* [x] **Criação de contas correntes** vinculadas a um usuário existente (um usuário pode ter mais de uma conta).
* [x] Funções refatoradas com uso de parâmetros posicionais e nomeados.

> A estrutura do sistema está preparada para evoluir com novos módulos como transferências, listagens, persistência e autenticação.

## 📄 Funcionalidades

* 💵 **Depósito**
* 💸 **Saque** (limite de R\$500 por transação e até 3 saques diários)
* 📃 **Extrato** com histórico de movimentações
* 👤 **Cadastro de usuário** (CPF é verificado para evitar duplicidade)
* 📆 **Criação de conta corrente** (número sequencial, agência fixa "0001")

## 📂 Estrutura de dados

* `usuarios`: lista de dicionários contendo os dados de cada usuário
* `contas`: lista de dicionários contendo agência, número da conta e o usuário vinculado

## 💡 Exemplo de entrada válida

```
Nome: Ana Souza
CPF: 12345678900
Data de nascimento: 01/01/1990
Endereço: Av. Central, 123 - Centro - Porto Alegre/RS
```

## ⚡ Como executar

1. Clone ou baixe este repositório
2. Acesse a pasta `sistema_v2`
3. Execute o script com:

```bash
python sistema_bancario_v2.py
```

## 📁 Pasta do projeto

Este código está localizado na pasta:

```
sistema_v2/
  ├── sistema_bancario_v2.py
  └── README.md
```

## 👤 Autor

**Francisco Goya**
Estudante de Análise e Desenvolvimento de Sistemas
Participante do Bootcamp Santander Backend com Python

[GitHub](https://github.com/FranciscoGoyaAMC) | [LinkedIn](https://www.linkedin.com/in/francisco-goya-de-almeida-martins-costa-0a8ab9327/)

---

Este projeto continua em evolução! ✨
