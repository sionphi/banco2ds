import json
import random


def exportar_conta(contaInteira):
    try:
        with open('conta.json', 'w', encoding="utf-8") as arquivo:
            json.dump(contaInteira, arquivo, ensure_ascii=False, indent=4)
        print("✔️ Conta salva com sucesso em 'conta.json'")
    except PermissionError:
        print('❌ Erro: Feche o arquivo para eu conseguir salvar!')


conta = []
saldo = 0


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
            novo['Saldo'] = '0'
            novo['Extrato']

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
                print("❌ Nenhuma conta salva ainda!")
        elif op == 3:
            if conta:
                exportar_conta(conta)
            break
        else:
            print("❌ Opção inválida!")


def depositar():
    contaDigitada = int(input("Digite o valor da sua conta"))
    senhaDigitada = int(input("Digite o valor da sua senha"))

    if contaDigitada == conta and senhaDigitada == novo[] :
        saldoDepositado = int(input("Digite o valor que você quer depositar: "))
        saldo += saldoDepositado

def sacar():
    contaDigitada = int(input("Digite o valor da sua conta"))
    senhaDigitada = int(input("Digite sua senha"))
    if contaDigitada == conta and  saldo > 0 and (novo['Senha']) == senhaDigitada:
        with open('conta.json', 'w' encoding='utf-8') as arquivoJson:

opcao = int(input("O que deseja fazer? 1 - Cadastro | 2 - Sacar:  | 3 - Depositar"))

match opcao:
    case 1:
        cadastro()
    case 2:
        sacar()
    case 3:
        depositar()
    case _:
        print("❌ Opção não encontrada!")
