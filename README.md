# Banco Python

## Descrição

Este projeto é um **sistema bancário simples** implementado em Python. Ele simula operações bancárias básicas, como **depósito**, **saque**, e **consulta de extrato**. O código tem como objetivo fornecer uma prática de desenvolvimento e reforçar o aprendizado dos conceitos de programação como controle de fluxo, manipulação de dados e funções.

### Funcionalidades:
- **Depositar**: Permite que o usuário deposite um valor na conta.
- **Sacar**: Permite que o usuário faça saques, respeitando o limite diário de saques e o limite de valor por saque.
- **Extrato**: Exibe todas as movimentações realizadas, como depósitos e saques, junto com o saldo atual.
- **Limites**: 
  - **Limite de saque por operação**: R$ 500,00.
  - **Limite de saques diários**: 3 saques.

---

## Projeto de Aprendizagem

Este é um **projeto de aprendizagem** realizado no **Bootcamp Suzano da DIO (Digital Innovation One)**. O objetivo principal deste projeto é aprender e aplicar conceitos de programação em Python, como estruturas de controle, funções e manipulação de dados.

---

## Como Executar

### Requisitos

- Python 3.x (Certifique-se de ter o Python 3.x instalado em sua máquina).

### Passos para Execução

1. **Baixar ou Clonar o Repositório**:
   - Caso esteja utilizando Git, execute:
     ```bash
     git clone https://github.com/c4rl0sfilho/DesafioBancoPythonDio.git
     ```
   - Caso esteja baixando manualmente, baixe o arquivo Python `banco_python.py`.

2. **Executar o Código**:
   - Navegue até a pasta onde o arquivo foi salvo e execute o código:
     ```bash
     python banco_python.py
     ```

3. **Interação com o Programa**:
   - O programa apresentará um menu com as opções:
     - **[d] Depositar**: Depositar um valor na conta.
     - **[s] Sacar**: Fazer um saque, respeitando os limites.
     - **[e] Extrato**: Consultar o extrato da conta.
     - **[q] Sair**: Encerrar o programa.

4. **Fechar o Programa**:
   - Para sair do programa, basta escolher a opção **[q]** e ele exibirá uma mensagem de despedida.

---

## Exemplo de Execução

```bash
+++++ Banco Python +++++

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> d
Informe o valor do depósito: 100
Depósito realizado com sucesso!

+++++ Banco Python +++++

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> s
Informe o valor do saque: 50
Saque realizado com sucesso!

+++++ Banco Python +++++

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> e

===== Extrato =====
Depósito: R$ 100.00
Saque: R$ 50.00

Saldo: R$ 50.00
===================

```
## Contribuição

Este é um projeto voltado para aprendizado, mas se você quiser melhorar ou contribuir com sugestões, fique à vontade para enviar um pull request.
