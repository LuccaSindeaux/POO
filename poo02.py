class Conta:
    numero='0000'
    saldo=0.0
    def __init__(self,numero,saldo,nome):
        self.numero=numero
        self.saldo=saldo
        self.nome=nome
        
    def listar(self):
        print('=============================================')
        print(f'Cliente: {self.nome}.\nConta Corrente {self.numero}.\nSaldo {self.saldo}.')
        print('=============================================')

    def depositar(self,valor):
        self.saldo +=valor
    def saque(self,valor):
        self.saldo-= valor

def entrada():
    nome=input('Digite o nome do cliente: ')
    numero=int(input('Digite o número da conta:'))
    saldo=float(input('Digite o valor da conta R$'))
    return (nome,numero,saldo)

list_user=[]
list_num=[]
list_saldo=[]

conta_lisi=Conta('654125-5',7000.89,'Lisiane')
# conta_lisi.numero='4564-5'
# conta_lisi.saldo=7000.89
conta_lisi.listar()

conta_murilin=Conta("9874-4",200000.02,'Murilin')
# conta_murilin.numero="9874-4"
# conta_murilin.saldo=200000.02
conta_murilin.listar()

conta_gugu=Conta('5555-6',10000000.99,'É o Gugu')
# conta_gugu.numero='5555-6'
# conta_gugu.saldo=10000000.99
conta_gugu.listar()

conta_nina=Conta('9999-0',500000.87,'Last Romantic Lesbian' )
# conta_nina.numero='9999-0'
# conta_nina.saldo=500000.87
conta_nina.listar()

conta_mrraguse=Conta('4563-7',23000.45,"É de cair os Butiá do bolso")
conta_mrraguse.listar()

conta_nina.saque(8000.56)
conta_murilin.saque(100000.50)
conta_nina.listar()
conta_murilin.listar()