import datetime as time

class Caminhao:
    def __init__(self,modelo,placa,carga):
        self.modelo=modelo
        self.placa=placa
        self.carga=carga

    def carregar(self,peso):
        peso=int(input('Qual o peso da carga, em quilos, adicionada? '))
        if peso > self.carga:
            print('Aí não né mano')
        else:
            print(f'Boa meu consagrado, carga adicionada com sucesso.\nCarga atual: {self.peso}Kg.')
    
    def desacarregar(self,peso):
        peso=int(input('Qual peso da carga que será removida do caminhão? '))
        self.peso-=peso
        print(f'Peso removido, carga atual: {self.peso}.')

class Motorista:
    def __init__(self,nome,idade,cnh,validade):
        self.nome=nome
        self.idade=idade
        self.cnh=cnh
        self.validade=validade
        self.movimento=None

        def dirigir(self):
            self.movimento ==True
        
        def frear(self):
            self.movimento ==False
            print('O caminhão está parado.')
        
        def verificarValidade(self):

