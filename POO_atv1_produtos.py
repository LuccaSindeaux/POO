'''
Crie uma classe Produto que represente um produto em um sistema de vendas. A classe deve ter os seguintes atributos:
codigo: inteiro que representa o código único do produto                                      ex.1
nome: string que representa o nome do produto                                                 ex. CAMISA
categoria: string que representa a categoria do produto                                       ex. Vestuário
preco: valor real que representa o preço do produto                                           ex. 79.90
quantidadeEstoque: inteiro que representa a quantidade do produto em estoque                  ex. 75

E os seguintes métodos:
__init__(self, codigo, nome, descricao, preco, quantidadeEstoque): construtor da classe que inicializa todos os atributos
get_codigo(self): retorna o código do produto
get_nome(self): retorna o nome do produto
get_categoria(self): retorna a descrição do produto
get_preco(self): retorna o preço do produto
get_quantidade_estoque(self): retorna a quantidade do produto em estoque
set_preco(self, novo_preco): define o novo preço do produto
vender(self, quantidade_vendida): diminui a quantidade do produto em estoque de acordo com a quantidade vendida (deve verificar se há estoque suficiente antes de realizar a venda
listar(self): 
- nome,
- a categoria,
- quantidade_vendida,
- preco e
- total_venda = o valor da venda quantidade_vendida * preco 
comprar(self, quantidade_comprada): aumenta (soma) na quantidade do produto em estoque de acordo com a quantidade comprada. 
'''

class Produto:
    def __init__ (self,codigo,nome,categoria,preco,quantidadeEstoque):
        self.codigo=codigo # ex:1
        self.nome=nome     # ex:CAMISA
        self.categoria=categoria #ex: vestuário
        self.preco=preco         #ex: 79.90
        self.quantidadeEstoque=quantidadeEstoque #ex: 75
        self.quantidade_vendida=0
    
    def get_codigo(self):
        print(f'Código do produto: {self.codigo}')

    def get_nome(self):
        print(f'Produto: {self.nome}')

    def get_categoria(self):
        print(f'Tipo de produto: {self.categoria}')

    def get_preco(self):
        print(f'Preço de {self.nome} é {self.preco}')

    def get_quantidade_estoque(self):
        print(f'Há {self.quantidadeEstoque} unidades deste produto em estoque.')

    def set_preco(self, novo_preco):
        if novo_preco >0:
            self.preco=novo_preco
        else:
            print('O novo preço tem que ser maior que zero.')

    def vender(self, quantidade_vendida):
        if quantidade_vendida <= self.quantidadeEstoque:
            self.quantidadeEstoque-=quantidade_vendida
            print(f'Foram vendidos {quantidade_vendida} unidades.\nEstoque atual de {self.nome}: {self.quantidadeEstoque} unidades.')
        else:
            print('Valor digitado é maior que a quantidade em estoque do produto.')

    def listar (self):
        total_venda=self.quantidade_vendida * self.preco
        print('-'*60)
        print(f'Listando as informações de {self.nome}:')
        print(f'Nome: {self.nome}.\nCategoria do produto: {self.categoria}.\nQuantidade vendida: {self.quantidade_vendida} unidades.\nPreço: R${self.preco:.2f}.\nTotal dos itens vendidos: R${total_venda:.2f}.')
        print('-'*60)

    def comprar(self, quantidade_comprada):
        quantidade_comprada=int(input(f'Quantos {self.nome} foram comprados? '))
        self.quantidadeEstoque+=quantidade_comprada
        print(f'estoque atual: {self.quantidadeEstoque}.')
    

#Testando com Livro
livro = Produto(101, "O Senhor dos Anéis", "Livros", 59.90, 30)
livro.get_categoria()
livro.listar()
livro.vender(15)
livro.get_quantidade_estoque()
livro.listar()

#Testando com ferramentas e forçando um erro na função vender
ferramenta1=Produto(789, 'Furadeira', 'Ferramenta',161.90,150)
ferramenta1.listar()
ferramenta1.vender(151)

#Mudando o preço de um jogo que entrou em promoção 
game1=Produto(1002,'Borderlands 3',"Video Game", 200.00, 320)
game1.listar()
game1.set_preco(130.50)
game1.listar()

#Testando demais comandos
livro.get_nome()
livro.get_codigo()
ferramenta1.get_nome()
ferramenta1.get_codigo()
game1.get_nome()
game1.get_codigo()