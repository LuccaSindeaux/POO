from animal import Animal

class Cachorro(Animal):
  def __init__(self, nome, idade, raca):
    super().__init__(nome, idade) #pega os atributos da classe pai
    self.raca = raca

  def emitir_som(self):
    print(f"{self.nome} está latindo!")
