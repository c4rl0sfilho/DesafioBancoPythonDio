# 🏦 Banco Python

Um projeto simples de **simulação de banco em Python**, feito totalmente via terminal.  
Permite criar usuários, abrir contas correntes, realizar depósitos, saques e consultar extratos — tudo com controle de limite diário de transações e validações automáticas.

---

## 🚀 Funcionalidades

✅ **Criar Usuário**  
- Cada usuário possui: nome, CPF (único), data de nascimento e endereço.  
- O endereço segue o formato: `logradouro, número - bairro - cidade/sigla`.

✅ **Listar Usuários**  
- Exibe todos os usuários cadastrados no sistema.

✅ **Criar Conta Corrente**  
- Cada conta é vinculada a um usuário existente.  
- Agência fixa: `0001`.  
- Número da conta é sequencial, começando em 1.  
- Um usuário pode ter várias contas, mas uma conta só pode ter um titular.

✅ **Depósito**  
- Realiza depósitos apenas com valores positivos.  
- Registra a operação no extrato.

✅ **Saque**  
- Permite saques até o valor disponível em saldo.  
- Registra a operação no extrato.

✅ **Extrato**  
- Mostra todas as movimentações (saques e depósitos) e o saldo atual.

✅ **Limite de Transações Diárias**  
- Cada usuário pode realizar **até 10 transações por dia**, incluindo saques e depósitos.  
- O limite é automaticamente reiniciado a cada novo dia.

---

## 🧩 Estrutura de Dados

### Usuário
```python
{
    "nome": "Carlos Silva",
    "cpf": "11111111111",
    "data_nascimento": "01/01/1990",
    "endereco": "Rua Exemplo, 123 - Centro - São Paulo/SP"
}
```
###Conta Corrente
```python
{
    "agencia": "0001",
    "numero_conta": 1,
    "usuario": <referência ao usuário>
}
```
💻 Como Executar o Projeto

1️⃣ Clone o repositório
```
git clone https://github.com/seu-usuario/banco-python.git
```

2️⃣ Acesse o diretório
```
cd banco-python
```
3️⃣ Execute o código
```
python banco.py
```

⚠️ Certifique-se de ter o Python 3.8+ instalado.

🧠 Conceitos Utilizados

Funções positional-only, keyword-only e positional + keyword

Estruturas de dados com listas e dicionários

Controle de fluxo e validação de entradas

Manipulação de datas com datetime

Limpeza de terminal com os.system()

Controle de tempo com time.sleep()

## Projeto de Aprendizagem

Este é um **projeto de aprendizagem** realizado no **Bootcamp Suzano da DIO (Digital Innovation One)**. O objetivo principal deste projeto é aprender e aplicar conceitos de programação em Python, como estruturas de controle, funções e manipulação de dados.

---

