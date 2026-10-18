from veiculos import *
from pedagio import * 
from salvar import salvar_relatorio

# Cores
CIANO = '\033[96m'
AMARELO = '\033[93m'
NEGRITO ='\033[1m'
VERMELHO ='\033[91m'
ROXO ='\033[95m'
VERDE ='\033[92m'
RESET = '\033[0m'

# Cria a praça de pedágio
praca = PracaPedagio()

# main
while True:
    print(f'\n{CIANO}{NEGRITO} ==== SISTEMA DE PEDÁGIO ===={RESET}')
    print(f'{VERMELHO}1 - Registrar Carro{RESET}')
    print(f'{VERDE}2 - Registrar Caminhão{RESET}')
    print(f'{ROXO}3 - Registrar Moto{RESET}')
    print(f'{AMARELO}4 - Mostrar Relatório {RESET}')
    print(f'{CIANO}5 - Salvar Relatório{RESET}')
    print('0 - Encerrar')

    opcao = input('Escolha uma opção: ')

    if opcao == '0':
        print('Sistema de Pedágio encerrado.')
        break

    elif opcao == '1':
        placa = input('Digite a placa: ')
        modelo = input('Digite o modelo do carro: ')
        eixos = int(input('Digite a quantidade de eixos: '))

        veiculo = Carro(placa,modelo,eixos)
        praca.registrar_veiculo(veiculo)
        print(f'{VERMELHO}Carro registrado com sucesso!!{RESET}')

    elif opcao == '2':
        placa = input('Digite a placa: ')
        modelo = input('Digite o modelo do caminhão: ')
        eixos = int(input('Digite a quantidade de eixos: '))

        veiculo = Caminhao(placa, modelo, eixos)
        praca.registrar_veiculo(veiculo)
        print(f'{VERDE}Caminhão registrado com sucesso!!{RESET}')

    elif opcao == '3':
        placa = input('Digite a placa: ')
        modelo = input('Digite o modelo da moto: ')
        eixos = int(input('Digite a quantidade de eixos: '))

        veiculo = Moto(placa, modelo, eixos)
        praca.registrar_veiculo(veiculo)
        print(f'{ROXO}Moto registrado com sucesso!!{RESET}')

    elif opcao == '4':
        praca.mostrar_relatorio()

    elif opcao == '5':
        salvar_relatorio(praca)
        print(f'{CIANO}Relatório salvo.{RESET}')

    else:
        print('Opção invalida! Tente novamente.')




