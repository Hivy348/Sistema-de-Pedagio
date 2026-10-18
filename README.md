# Sistema-de-Pedagio  
Esse projeto simples foi desenvolvido como treinamento de Programação Orientada a Objetos.  
O sistema precisava ser composto por:  
- Classes e Objetos
- Herança
- Modularização
- Persistência em arquivo
- Métodos e atributos
- Encapsulamento simples
- Cálculos automáticos

  # Estrutura do Projeto  
  projeto_pedagio/  
  |  
  |__ veiculos.py  
  |__ pedagio.py  
  |__ salvar.py  
  |__ main.py  

  # Herança(veiculos.py)
  - Método construtor com placa, modelo e eixos
  - Função calcular pedágio sem nenhum atributo
  - Subclasses:
    Herda o método construtor
    Classe Carro - Valor fixo do pedágio: R$ 12,00 em calcular pedagio  
    Classe Moto - Valor fixo do pedágio: R$ 6,00 em calcular pedágio    
    Classe Caminhão - Valor fixo do pedágio: R$ 10,00 por eixo em calcular pedágio   

    # Persistência(salvar.py)     
    - Cria um arquivo .txt contendo data e hora, lista de veículos e total arrecadado.
    - Importa a biblioteca datetime e os arquivos veiculos.py e pedagio.py
    
    # Pedagio.py
    - Método construtor com self.veiculo e self.total_arrecadado
    - Registrar_veiculo com data e hora, adição do veiculo e calculo do total arrecadado
    - Mostrar_relatorio com um laço for imprimindo placa, modelo, eixo, data e hora
    - Imprimi quantidade de veiculos e total arrecadado
    
    # Arquivo Principal(main.py)    
    - Cores(vermelho, verde, amarelo, roxo, ciano, negrito, reset)   
    - Criação da praça
    - Registrar Carro(placa, modelo, eixos)  
    - Registrar Caminhão(placa, modelo, eixos)      
    - Registrar Moto(placa, modelo, eixos)        
    - Mostrar Relatório(numeração, placa, modelo, eixos, quantidade de veículos, total arrecadado)  
    - Salvar relatório    
    - Encerrar    
