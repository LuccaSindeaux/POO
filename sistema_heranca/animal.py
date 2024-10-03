class Animal:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  def emitir_som(self):
    print(f"{self.nome} está emitindo som!")
    pass  # Implementar em cada classe filha