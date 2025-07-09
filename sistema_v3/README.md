# 💰 Sistema Bancário em Python – Versão 3

Este projeto é a **versão 3** do sistema bancário desenvolvido como parte dos meus estudos em Python, voltado ao domínio de orientação a objetos, modularização, boas práticas de programação e validações com expressões regulares.

---

## 🧠 Objetivo

Simular o funcionamento básico de um sistema bancário, permitindo ao usuário criar clientes e contas, realizar depósitos, saques, consultar extratos e aplicar regras de negócio como limites de saque e validações de entrada.

---

## 🚀 Funcionalidades

* ✅ Criar cliente com validações de CPF, data de nascimento e endereço.
* ✅ Criar conta corrente atrelada a um cliente existente.
* ✅ Depositar valores na conta.
* ✅ Sacar valores com controle de:

  * Limite de valor por transação (`R$500`)
  * Limite de saques diários (`3`)
* ✅ Consultar extrato com histórico de transações.
* ✅ Menu interativo em terminal.

---

## 🧱 Estrutura do Projeto

* `Cliente` e `PessoaFisica`: Representam o cliente do banco.
* `Conta` e `ContaCorrente`: Gerenciam saldo, número da conta, saques e depósitos.
* `Transacao`, `Saque` e `Deposito`: Usam o padrão Command para registrar ações.
* `Historico`: Armazena todas as transações realizadas.
* `Validador`: Realiza validações com Expressões Regulares.
* `Filtros`: Busca clientes e contas de forma eficiente.
* `Operacoes`: Lógica de negócios separada do menu principal.
* `Menu`: Interface simples via terminal.
* `main()`: Ponto de entrada do sistema.

---

## 🔒 Validações com Regex

* **CPF**: Somente 11 dígitos numéricos.
* **Data de Nascimento**: Formato `dd/mm/aaaa`.
* **Endereço**: Formato `Rua, Número - Bairro - Cidade/UF` (com suporte a acentuação).

---

## 📦 Como Executar

1. Certifique-se de ter Python 3 instalado.

2. Clone o repositório:

   ```bash
   git clone https://github.com/FranciscoGoyaAMC/BootCampSantander2025
   cd BootCampSantander2025/sistema_v3
   ```

3. Execute o script:

   ```bash
   python sistema_bancario_v3.py
   ```

---

## 🛠️ Tecnologias e Conceitos Usados

* Python 3
* Programação Orientada a Objetos (POO)
* Abstração e Herança
* Polimorfismo com classes abstratas
* Expressões Regulares (`re`)
* Boas práticas de modularização e legibilidade

---

## 📚 Aprendizados

Durante o desenvolvimento desta versão, aprofundei meu conhecimento em:

* Separação de responsabilidades entre classes
* Criação de código mais escalável e reutilizável
* Uso de regex para validação de dados no terminal
* Princípios de design de software (cohesion e single-responsibility)

---

## 👨‍💻 Autor

Desenvolvido por **Francisco Goya**, estudante de Análise e Desenvolvimento de Sistemas e entusiasta de desenvolvimento backend com Python.

📌 [LinkedIn](https://www.linkedin.com/in/francisco-goya-de-almeida-martins-costa-0a8ab9327/)
📌 [GitHub](https://github.com/FranciscoGoyaAMC)
