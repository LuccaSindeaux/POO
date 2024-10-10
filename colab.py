'''
**Exercício de Herança em Programação Orientada a Objetos em Python**
**Objetivo:** Praticar a criação de classes, herança e uso de métodos em Python.
**Descrição:**
Você foi contratado para desenvolver um sistema simples de gerenciamento de veículos para uma locadora de veículos. O sistema deve ser capaz de lidar com diferentes tipos de veículos, como carros e motos, e calcular o valor do aluguel com base no tipo de veículo e na quantidade de dias alugados.
**Requisitos:**
1. **Classe Base - Veiculo:**
   - Crie uma classe chamada `Veiculo` que tenha os seguintes atributos:
     - `marca` (string)
     - `modelo` (string)
     - `ano` (inteiro)
     - `preco_diaria` (float)
   - A classe deve ter um método chamado `calcular_aluguel` que recebe o número de dias e retorna o valor total do aluguel.
2. **Classe Derivada - Carro:**
   - Crie uma classe chamada `Carro` que herda de `Veiculo`.
   - Adicione um atributo adicional chamado `numero_portas` (inteiro).
   - Sobrescreva o método `calcular_aluguel` para aplicar um desconto de 10% se o aluguel for por mais de 7 dias.
3. **Classe Derivada - Moto:**
   - Crie uma classe chamada `Moto` que herda de `Veiculo`.
   - Adicione um atributo adicional chamado `cilindrada` (inteiro).
   - Sobrescreva o método `calcular_aluguel` para aplicar uma taxa adicional de 5% devido ao seguro de acidentes.
**Instruções:**
1. Implemente as classes `Veiculo`, `Carro` e `Moto` conforme especificado.
2. Crie instâncias de `Carro` e `Moto` e demonstre o uso de seus métodos, incluindo o cálculo do valor do aluguel.
3. Certifique-se de que os métodos sobrescritos considerem os cálculos adicionais (desconto para carros e taxa adicional para motos).
**Exemplo de Uso:**
```python
# Criação de um carro
carro = Carro(marca="Toyota", modelo="Corolla", ano=2020, preco_diaria=150.0, numero_portas=4)
valor_aluguel_carro = carro.calcular_aluguel(dias=10)
print(f"Valor do aluguel do carro por 10 dias: R${valor_aluguel_carro:.2f}")
# Criação de uma moto
moto = Moto(marca="Honda", modelo="CB500", ano=2019, preco_diaria=100.0, cilindrada=500)
valor_aluguel_moto = moto.calcular_aluguel(dias=5)
print(f"Valor do aluguel da moto por 5 dias: R${valor_aluguel_moto:.2f}")
'''

class Veiculo:
    def __init__ (self,marca,modelo,ano, preco_diaria):
        self.marca=marca
        self.modelo=modelo
        self.ano=ano
        self.preco_diaria=preco_diaria

    def calcular_aluguel(self,dias):
        aluguel=dias*self.preco_diaria
        print(f" valor do aluguel para {dias} será de {aluguel:.2f} reais.")

class Carro(Veiculo):
    def __init__ (self, marca,modelo,ano, preco_diaria, numero_portas):
        super().__init__(marca,modelo,ano,preco_diaria)
        self.numero_portas=numero_portas
    
    def calcular_aluguel(self,dias):
        valor = super().calcular_aluguel(dias)
        if dias >7:
            valor_novo=valor*0.90
            print(f'Valor com 10% de desconto: {valor_novo} reais')
        else:
            print(f" valor do aluguel para {dias} será de {valor:.2f} reais.")

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, preco_diaria, cilindrada):
        super().__init__(marca, modelo, ano, preco_diaria)
        self.cilindrada=cilindrada

    def calcular_aluguel(self,dias):
        valor = super().calcular_aluguel(dias)
        valor_novo=valor*1.05
        print(f" valor do aluguel para {dias} será de {valor_novo:.2f} reais.")


moto1=Moto('Maverick','Street',2007,160.55,4)
moto1.calcular_aluguel(5)

carro1=Carro('Toyota','Sedan',2008,100.00,4)
carro1.calcular_aluguel(6)