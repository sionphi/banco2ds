import json
import random

def exportar_conta(contaInteira):
    try:
        with open('conta.json', 'w', encoding='utf-8') as arquivo:
            json.dump(contaInteira, arquivo, indent=4)

        print("✔️ Conta salva com sucesso em 'conta.json'")

    except PermissionError:
        print("❌ Erro: Feche o arquivo para eu conseguir salvar!")

conta = []

def cadastro():
    while True:
        print("\n[1] Criar conta | [2] Ver conta | [3] Salvar e Sair")
        op = int(input("Escolha: "))
        if op == 1:
            novo = {}
            novo['Nome'] = input("Nome: ")
            novo['Senha'] = random.randint(1000000000, 99999999999)
            novo['Agencia'] = '0001'
            novo['Conta'] = random.randint(1000000000, 99999999999)
            novo['Cpf'] = input("Digite o número do CPF: ")
            novo['Cep'] = input("Digite seu CEP: ")
            novo['Saldo'] = 0
            novo['Extrato'] = []
            print(f'A sua senha é {novo["Senha"]}, guarde bem')
            conta.append(novo)
            print("✔️ Conta criada com sucesso!")
        elif op == 2:
            try:
                with open("conta.json", 'r', encoding='utf-8') as arquivoJson:
                    save = json.load(arquivoJson)
                    print("\n--- CONTAS SALVAS ---")
                    for pessoa in save:
                        print(pessoa)
            except FileNotFoundError:
                print("Nenhuma conta salva")
        elif op == 3:
            if conta:
                exportar_conta(conta)
            break
        else:
            print("Opção inválida!")
def encontrar_conta(numero_conta, senha):
    pessoaEncontrada = {}
    for pessoa in conta:
        if pessoa['Conta'] == numero_conta and pessoa['Senha'] == senha:
            pessoaEncontrada = pessoa
    return pessoaEncontrada
    
def depositar():
    contaDigitada = int(input("Digite o número da sua conta: "))
    senhaDigitada = int(input("Digite sua senha: "))
    pessoa = encontrar_conta(contaDigitada, senhaDigitada)
    if pessoa:
        valor = float(input("Digite o valor que você quer depositar: R$ "))
        if valor > 0:
            pessoa['Saldo'] += valor
            pessoa['Extrato'].append({
                'Tipo': 'Depósito',
                'Valor': valor,
                'Saldo após operação': pessoa['Saldo']
            })
            exportar_conta(conta)
            print(f"Depósito de R$ {valor} realizado!")
            print(f"Saldo atual: R$ {pessoa['Saldo']}")
        else:
            print("O valor precisa ser maior que zero!")
    else:
        print("Conta ou senha incorreta!")

def sacar():
    contaDigitada = int(input("Digite o número da sua conta: "))
    senhaDigitada = int(input("Digite sua senha: "))
    pessoa = encontrar_conta(contaDigitada, senhaDigitada)
    if pessoa:
        if pessoa['Saldo'] > 0:
            valor = float(input("Digite o valor que você quer sacar: R$ "))
            if valor <= 0:
                print("digita um valor acima de 0")
            elif valor > pessoa['Saldo']:
                print("Sem saldo")
            else:
                pessoa['Saldo'] -= valor
                pessoa['Extrato'].append({
                    'Tipo': 'Saque',
                    'Valor': valor,
                    'Saldo após operação': pessoa['Saldo']
                })
                exportar_conta(conta)
                print(f"Saque de R$ {valor} realizado!")
                print(f"Saldo atual: R$ {pessoa['Saldo']}")
        else:
            print("Nao tem saldo para sacar")
    else:
        print("senha incorreta")

def ver_extrato():
    contaDigitada = int(input("Digite o número da sua conta: "))
    senhaDigitada = int(input("Digite sua senha: "))
    pessoa = encontrar_conta(contaDigitada, senhaDigitada)
    if pessoa:
        print("\n========== EXTRATO ==========")
        print(f"Titular: {pessoa['Nome']}")
        print(f"Conta: {pessoa['Conta']}")
        print(f"Saldo atual: R$ {pessoa['Saldo']}")
        print("------------------------------")
        else:
            for movimento in pessoa['Extrato']:
                print(f"Tipo: {movimento['Tipo']}")
                print(f"Valor: R$ {movimento['Valor']}")
                print(f"Saldo: R$ {movimento['Saldo após operação']}")
                print("------------------------------")
    else:
        print("senha incorreta")
opcao = int(input(
    "O que deseja fazer?\n"
    "1 - Cadastro | 2 - Sacar | 3 - Depositar | 4 - Ver extrato"
))
match opcao:
    case 1:
        cadastro()
    case 2:
        sacar()
    case 3:
        depositar()
    case 4:
        ver_extrato()
    case _:
        print("❌ Opção não encontrada!")
