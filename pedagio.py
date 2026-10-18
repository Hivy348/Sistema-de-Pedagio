from datetime import datetime
from veiculos import *
class PracaPedagio:

    def __init__(self):
        self.veiculo = [] 
        self.total_arrecadado = 0
    
    def registrar_veiculo(self,veiculo):
        veiculo.data_hora = datetime.now()

        self.veiculo.append(veiculo) 
        self.total_arrecadado += veiculo.calcular_pedagio()

    def mostrar_relatorio(self):

        print(f'\n=== RELATÓRIO PEDÁGIO ===\n')

        for i, veiculos in enumerate(self.veiculo, start = 1):
            print(f'Veiculo {i}')
            print(f'Placa: {veiculos.placa}')
            print(f'Modelo: {veiculos.modelo}')
            print(f'Eixo: {veiculos.eixos}\n')
            print(f'Data e hora: ' f'{veiculos.data_hora.strftime("%d/%m/%Y  %H:%M:%S")}')
        
        print(f'Quantidade de veículos presentes:{len(self.veiculo)}\n')
        print(f'Total Arrecadado: R${self.total_arrecadado:.2f}\n')