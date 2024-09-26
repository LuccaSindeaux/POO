'''
Crie um sistema simples de gerenciamento de uma transportadora utilizando programação orientada a objetos em Python.
Requisitos:
1) Classe Caminhão:
Atributos: modelo, placa, capacidade_carga.
Métodos: carregar(peso), descarregar(peso). O método carregar deve verificar se o peso a ser carregado não excede a capacidade do caminhão.

2) Classe Motorista:
Atributos: nome, idade, CNH. dataValidade
Métodos: dirigir(caminhao). Este método deve imprimir uma mensagem indicando que o motorista está dirigindo o caminhão.
verificarValidade(motorista)

3) Associação entre as classes:
Um caminhão deve ser dirigido por apenas um motorista.
Um motorista pode dirigir vários caminhões.

Exercícios:
Crie pelo menos 3 objetos da classe Caminhão e 2 objetos da classe Motorista.
Atribua um motorista a cada caminhão.
Simule a carga e descarga de um caminhão.
verifique se a CNH do Motorista é stá valida, caso estiver para vencer em 30 dias ou vencida verificar se o motorista está associado a um caminhão e avisar para renovar a CNH
Imprima na tela informações sobre os caminhões e seus respectivos motoristas.

Dicas:
Utilize a associação entre as classes para conectar um objeto caminhão a um objeto motorista.
Explore os métodos de cada classe para simular as ações da transportadora.
Utilize a orientação a objetos para modelar o problema de forma clara e organizada.
Exemplo de saída:
Caminhão:
  -Modelo: Mercedes Benz
  -Placa: AAA-1234
  -Capacidade de carga: 10000 kg
  -Motorista: João Silva
  -Carga atual: 5000 kg

Desafios:
- Adicione um atributo "carga_atual" à classe Caminhão para controlar o peso carregado.
- Implemente um método para calcular o frete de um transporte com base na distância e no peso da carga.
- Crie uma classe "Viagem" para armazenar informações sobre as viagens realizadas pelos caminhões.

Este exercício tem como objetivo:
Fortalecer a compreensão sobre a associação entre classes em Python.
Aplicar os conceitos de programação orientada a objetos em um cenário real.
Desenvolver a lógica de programação e a capacidade de resolver problemas.
Bons estudos!
'''

import datetime

class Caminhao:
    def __init__(self,modelo,placa,carga):
        self.modelo=modelo
        self.placa=placa
        self.carga=carga
        self.carga_atual=0
        self.motorista=None

    def carregar(self,peso):
        peso=int(input('Qual o peso da carga, em quilos, adicionada? '))
        if peso > self.carga:
            print('Aí não né mano')
        else:
            print(f'Boa meu consagrado, carga adicionada com sucesso.\nCarga atual: {self.peso}Kg.')
    
    def desacarregar(self,peso):
        peso=int(input('Qual peso da carga que será removida do caminhão? '))
        if self.peso <= self.carga_atual:
            self.varga_atual-=peso
            print(f'Peso removido, carga atual: {self.carga_atual}.')
        else:
            print('O peso digitado não é possível...')

class Motorista:
    def __init__(self,nome,idade,cnh,validade):
        self.nome=nome
        self.idade=idade
        self.cnh=cnh
        self.validade=validade
        self.caminhoes=[]
        self.validacao=None

        def verificar_cnh(self):
            atual=datetime.date.today()
            if self.validade < atual:
                print(f'A CNH de {self.nome} está vencida.')
                self.validacao=False
            elif self.validade >= atual:
                print(f'A CNH de {self.nome} está dentro da validade.')
                self.validacao=True
            return verificar_cnh

        def dirigir(self,caminhao):
            if self.validacao is True:
                caminhao.motorista=self
                self.caminhoes.append(caminhao)
                print(f'{self.nome} está dirigindo o caminhão {caminhao.modelo}.')
            else:
                print(f'{self.nome} não pode dirigir. CNH vencida ou prestes a vencer.')
            return dirigir
        


caminhao1 = Caminhao("Mercedes Benz", "AAA-1234", 10000)
caminhao2 = Caminhao("Volvo FH", "BBB-5678", 8000)
caminhao3 = Caminhao("Scania R450", "CCC-9876", 12000)

motorista1 = Motorista("João Silva", 45, "123456789", datetime.date(2024, 10, 15))
motorista2 = Motorista("Carlos Souza", 50, "987654321", datetime.date(2023, 9, 30))

motorista1.verificar_cnh()
motorista2.verificar_cnh()