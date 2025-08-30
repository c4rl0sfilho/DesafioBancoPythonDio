import time, os

menu = """
+++++ Banco Python +++++

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0.0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def depositar(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("Depósito realizado com sucesso!")
        time.sleep(1)
        clear_screen()
    return saldo

def sacar(valor, saldo, extrato, numero_saques):
    if numero_saques >= LIMITE_SAQUES:
        print("Número máximo de saques diários atingido.")
        return saldo, numero_saques

    if valor > saldo:
        print("Saldo insuficiente.")
        return saldo, numero_saques

    if valor > limite:
        print("Valor do saque excede o limite por operação.")
        return saldo, numero_saques

    if valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print("Saque realizado com sucesso!")
        time.sleep(1)
        clear_screen()
    else:
        print("Valor inválido para saque.")
        time.sleep(1)
        clear_screen()
    
    return saldo, numero_saques  

def exibir_extrato(saldo, extrato):
    print("\n===== Extrato =====")
    if not extrato:
        print("Nenhuma movimentação.")
    else:
        for item in extrato:
            print(item)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("===================\n")

while True:
    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Informe o valor do depósito: "))
        saldo = depositar(valor_deposito, saldo, extrato)
    
    elif opcao == "s":
        valor_saque = float(input("Informe o valor do saque: "))
        saldo, numero_saques = sacar(valor_saque, saldo, extrato, numero_saques)

    elif opcao == "e":
        exibir_extrato(saldo, extrato)

    elif opcao == "q":
        print("Obrigado por usar o Banco Python. Até logo!")
        break
