class Automovel:
    def __init__(self, marca, modelo, cilindrada, num_portas, cor):
        self.marca = marca
        self.modelo = modelo
        self.cilindrada = cilindrada
        self.num_portas = num_portas
        self.cor = cor
        self.velocidade = 0  # Inicializa a velocidade como zero
    def acelerar(self):
        self.velocidade += 10
        print(f"O automóvel {self.marca} {self.modelo} acelerou. Velocidade atual: {self.velocidade} km/h")
    def frear(self):
        if self.velocidade >= 10:
            self.velocidade -= 10
            print(f"O automóvel {self.marca} {self.modelo} freou. Velocidade atual: {self.velocidade} km/h")
        else:
            print("O automóvel já está parado.")
    def parar(self):
        self.velocidade = 0
        print(f"O automóvel {self.marca} {self.modelo} parou. Velocidade atual: {self.velocidade} km/h")
    def report(self):
        if self.velocidade ==0:
            print(f'O carro {self.marca} {self.modelo} está parado.')
        elif self.velocidade >=10:
            print(f'O automóvel {self.marca} {self.modelo} está a {self.velocidade}.')

# Exemplo de inicialização de objetos e uso dos métodos
carro1 = Automovel("Toyota", "Corolla", 2000, 4, "Prata")
carro2 = Automovel("Honda", "Civic", 1800, 4, "Preto")
carro1.acelerar()
carro1.acelerar()
# carro1.frear()
# carro1.parar()
carro1.report()
print('')
carro2.acelerar()
carro2.frear()
carro2.frear()
carro2.parar()
carro2.report()