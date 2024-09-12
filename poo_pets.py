'''
Objetivo: Criar uma classe em Python para representar animais de estimação, com os métodos:

Requisitos:
A classe deve se chamar AnimalEstimacao.
A classe deve ter os seguintes atributos:
nome: nome do animal
especie: espécie do animal (ex: cachorro, gato, peixe)
idade: idade do animal em anos
estado: estado que o animal se encontra (´Comendo', 'Dormindo','Brincando')
A classe deve ter os seguintes métodos:
__init__(self, nome, especie, idade): método construtor da classe, que inicializa os atributos
comer(): método que simula o animal comendo
dormir(): método que simula o animal dormindo
brincar(): método que simula o animal brincando
listar(): que retorna uma string com a representação textual do animal (ex: "Nome: Rex, Espécie: Cachorro, Idade: 3 anos,  Estado:Comendo").

Exemplo de uso
animal = AnimalEstimacao("Rex", "Cachorro", 3) animal.comer() animal.dormir() animal.brincar() animal.listar() 

Desafio:
Adicione mais métodos à classe para representar outros comportamentos dos animais de estimação (ex: latir, miar, nadar)
'''
# class AnimalEstimacao:
#     def __init__(self,nome,especie,idade):
#         self.nome=nome
#         self.especie=especie
#         self.idade=idade

#     def comer(self):
#         self.food=input('O pet está comendo? [S/N]').upper()
#         if self.food =='S':
#             self.food=True
#         else:
#             self.food=False
#     def dormir(self):
#         self.sleep=input('O pet está dormindo? [S/N]').upper()
#         if self.sleep =='S':
#             self.sleep=True
#         else:
#             self.sleep=False
#     def brincar(self):
#         self.play=input('O pet está brincando? [S/N]').upper()
#         if self.play =='S':
#             self.play=True
#         else:
#             self.play=False
    
#     def listar(self):
#         if self.food is True:


class AnimalEstimacao:
    def __init__(self, nome, especie, idade):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.estado = None  # Estado inicial do animal

    def comer(self):
        self.estado = "Comendo"
        print(f"{self.nome} está comendo.") # Atualiza o estado do animal para 'Comendo'

    def dormir(self):
        self.estado = "Dormindo"
        print(f"{self.nome} está dormindo.") # Atualiza o estado do animal para 'Dormindo'

    def brincar(self):
        self.estado = "Brincando"
        print(f"{self.nome} está brincando.") # Atualiza o estado do animal para 'Brincando'

    def listar(self):
        return (f"Nome: {self.nome}, Espécie: {self.especie}, Idade: {self.idade} anos, Estado: {self.estado}")
    
    #DESAFIO:
    def nadar(self):
        if self.especie.lower() == 'peixe':
            print(f'{self.nome} está nadando.')
        else:
            print(f'O pet {self.nome} não pode nadar...')
    def voar(self):
        if self.especie.lower() == 'pássaro' or self.especie.lower() == 'ave' :
            print(f'{self.nome} está voando.')
        else:
            print(f'O pet {self.nome} não pode voar...')
    def latir(self):
        if self.especie.lower() == 'cachorro':
            print(f'{self.nome} está latindo.')
        else:
            print(f'O pet {self.nome} não pode latir...')
    def miar(self):
        if self.especie.lower() == 'gato':
            print(f'{self.nome} está miando.')
        else:
            print(f'O pet {self.nome} não pode miar...')
        

# Exemplo de uso
animal = AnimalEstimacao("Rex", "Cachorro", 3)
print(animal.listar())  # Antes de realizar qualquer ação
animal.comer()
print(animal.listar())  # Após comer
animal.dormir()
print(animal.listar())  # Após dormir
animal.brincar()
print(animal.listar())  # Após brincar
animal.latir()
print(animal.listar()) # Fazer Rex latir
animal.miar()
print(animal.listar()) # Testando se Rex mia