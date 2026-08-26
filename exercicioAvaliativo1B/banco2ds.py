import json # É um formato de arquivo
import csv
import random

def exportar_conta(contaInteira):
    try:
        with open('conta.json', 'a', encoding="utf-8") as arquivo:
            gravador = json.writer(arquivo)
            json.dump(["Nome", "Senha", "Agencia", "Conta", "Cpf", 'Cep', 'Saldo'])
            for conta in contaInteira:
                json.dump([conta['Nome'], conta['Senha'], conta['Agencia'], conta["Conta"], conta['Cpf'], conta['Cep'], conta['Saldo']])
        print("✔️ Conta Salva com sucesso em 'conta.json'")
    except PermissionError:
        print('❌ error: Fecha o Excel para eu salvar o arquivo')

conta = []


def cadastro():
    while True:
        print("\n[1] Criar conta | [2] Ver conta | [3] Salvar e Sair")

        op = int(input("Escolha: "))
        if op == 1:
            novo = {}
            novo ['Nome'] = input("Nome: ")
            novo ['Senha'] = input('Senha: ')
            novo ['Agencia'] = '0001'
            novo ['Conta'] = (1)
            novo ['Cpf'] = int(input("Digite o numero do cpf"))
            novo ['Cep'] = int(input('Digite seu CEP'))
            novo ['Saldo'] = float(input('Digite seu saldo atual'))

            conta.append(novo)
            print('⚔️ Aventureiro pronto para o combate!')
        elif op == 2:
            with open("guilda.json", 'r', encoding='utf-8') as arquivoJson:
                save = json.load(arquivoJson)
                for conta in save:
                    conta.append(conta)
                print(conta)
        else:
            if conta: exportar_conta(conta)
            break
def ler():
    try:
        with open("historico.txt", 'r', encoding="utf-8") as arquivo:
            print("--- Relembrando a sua história ---")
            for indice, linha in enumerate(arquivo, 1):
                print(f'Dia {indice}: {linha.strip()}')
    except FileNotFoundError:
        print("❌ Erro: Arquivo não encontrado!")

def gravar():
    while True:
        entrada = input("O que conquistaste hoje? (ou 'fim' para salvar): ")
        if entrada.lower() == 'fim':
            break
        with open('historico.txt', 'a', encoding="utf-8") as arquivo:
            arquivo.write(f"- {entrada}\n")
    print('Conta atualizada com sucesso')

print('--- DIÁRIO DE MISSÕES ---')
opcao = int(input("O que deseja fazer? 1 - Ler | 2 - Gravar: "))
match opcao:
    case 1:
        cadastro()
    case 2:
        ler()
    case _:
        print("Opção não encontrada!")