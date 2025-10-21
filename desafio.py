import time
import os
import datetime

# ======= Configurações Iniciais =======
menu = """
+++++ Banco Python +++++

[n] Novo usuário
[l] Listar usuários
[c] Nova conta corrente
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

AGENCIA = "0001"
LIMITE_TRANSACOES_DIARIAS = 10

# ======= Dados Ficticios =======
usuarios = [
    {"nome": "Carlos Silva", "cpf": "11111111111", "saldo": 1500.0, "transacoes_hoje": 0, "data_transacao": datetime.date.today()},
    {"nome": "Ana Souza", "cpf": "22222222222", "saldo": 2300.0, "transacoes_hoje": 0, "data_transacao": datetime.date.today()},
    {"nome": "João Pereira", "cpf": "33333333333", "saldo": 500.0, "transacoes_hoje": 0, "data_transacao": datetime.date.today()},
]
contas = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def depositar(valor, saldo, extrato, /):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("✅ Depósito realizado com sucesso!")
        time.sleep(1)
        clear_screen()
    else:
        print("❌ Valor inválido para depósito.")
    return saldo, extrato

def sacar(*, valor, saldo, extrato):
    if valor <= 0:
        print("❌ Valor inválido para saque.")
    elif valor > saldo:
        print("❌ Saldo insuficiente.")
    else:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        print("✅ Saque realizado com sucesso!")
        time.sleep(1)
        clear_screen()
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n===== Extrato =====")
    if not extrato:
        print("Nenhuma movimentação registrada.")
    else:
        for item in extrato:
            print(item)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("===================\n")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")

    # Verifica duplicidade
    usuario_existente = next((u for u in usuarios if u["cpf"] == cpf), None)
    if usuario_existente:
        print("❌ Já existe um usuário com esse CPF.")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, nmr - bairro - cidade/sigla): ")

    usuarios.append({
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    })

    print("✅ Usuário criado com sucesso!")
    time.sleep(1)
    clear_screen()


def listar_usuarios(usuarios):
    print("\n===== Lista de Usuários =====")
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for i, usuario in enumerate(usuarios, start=1):
            print(f"\nUsuário {i}")
            print(f"Nome: {usuario['nome']}")
            print(f"CPF: {usuario['cpf']}")
            print(f"Data de Nascimento: {usuario['data_nascimento']}")
            print(f"Endereço: {usuario['endereco']}")
    print("=============================\n")


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)

    if not usuario:
        print("❌ Usuário não encontrado. Crie o usuário antes de abrir uma conta.")
        return None

    conta = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print(f"✅ Conta criada com sucesso! Agência: {agencia} | Número: {numero_conta}")
    time.sleep(1)
    clear_screen()
    return conta


def listar_contas(contas):
    print("\n===== Contas Correntes =====")
    if not contas:
        print("Nenhuma conta criada.")
    else:
        for conta in contas:
            print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | Titular: {conta['usuario']['nome']}")
    print("============================\n")

saldo = 0.0
extrato = []
total_transacoes = 0
data_transacoes = datetime.date.today()

while True:
    # --- Verifica se mudou o dia ---
    data_atual = datetime.date.today()
    if data_atual != data_transacoes:
        total_transacoes = 0
        data_transacoes = data_atual
        print("🌅 Novo dia detectado! Limite de transações diárias reiniciado.\n")

    opcao = input(menu)

    if opcao == "n":
        criar_usuario(usuarios)

    elif opcao == "l":
        listar_usuarios(usuarios)

    elif opcao == "c":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
        if conta:
            contas.append(conta)

    elif opcao == "d":
        if total_transacoes >= LIMITE_TRANSACOES_DIARIAS:
            print("⚠️ Limite diário de transações atingido. Tente novamente amanhã.")
            continue

        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(valor, saldo, extrato)
        total_transacoes += 1

    elif opcao == "s":
        if total_transacoes >= LIMITE_TRANSACOES_DIARIAS:
            print("⚠️ Limite diário de transações atingido. Tente novamente amanhã.")
            continue

        valor = float(input("Informe o valor do saque: "))
        saldo, extrato = sacar(valor=valor, saldo=saldo, extrato=extrato)
        total_transacoes += 1

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "q":
        print("👋 Obrigado por usar o Banco Python. Até logo!")
        break

    else:
        print("❌ Opção inválida, tente novamente.")
