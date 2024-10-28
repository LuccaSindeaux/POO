'''
AVALIAÇÃO 2 - CRUD Veículos 

    QUERY:
CREATE TABLE veiculos (
    ID_veiculo INT PRIMARY KEY AUTO_INCREMENT,
    marca VARCHAR(50),
    modelo VARCHAR(50),
    placa VARCHAR(20),
    ano INT,
    valor_diaria DECIMAL(10,2)
);

-----Criar funções: Crie funções para cada uma das operações (inserir, atualizar, excluir, listar).
Interface do usuário: Implemente uma interface simples para o usuário interagir com o programa, por exemplo, utilizando um menu com opções.

-----Dicas:
1)Tratamento de erros: Utilize try-except para tratar possíveis erros durante a conexão com o banco de dados ou execução de queries.
2)Validação de dados: Valide os dados inseridos pelo usuário para evitar erros e garantir a integridade dos dados.
3)Formatação de saída: Apresente os resultados das consultas de forma clara e organizada.
4)SQLAlchemy ORM: Explore o uso do SQLAlchemy ORM para mapear as classes Python para as tabelas do banco de dados.
5)Parametrização de queries: Utilize parâmetros para evitar SQL injection e melhorar a segurança.

Desafios Adicionais:

Implementar uma busca por veículos com base em critérios como marca, modelo ou período de locação.
Criar relatórios com informações sobre os veículos, como a média do valor da diária ou a quantidade de veículos por marca.
Implementar um sistema de login para controlar o acesso ao sistema.
Observação: Adapte o código acima às suas necessidades e configurações específicas do banco de dados.
'''

from sqlalchemy import create_engine, Column, Integer, String, Numeric
from sqlalchemy.orm import sessionmaker, declarative_base


# Configurações do banco de dados                      nome do banco: 
DATABASE_URL ="mysql+mysqlconnector://root:@localhost/aluguel_veiculos"

# Criação do engine e da sessão
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Execução do programa
if __name__ == "__main__":
    Base.metadata.create_all(engine)

class Veiculo(Base):
    __tablename__ = 'veiculos'

    ID_veiculo = Column(Integer, primary_key=True, autoincrement=True)
    marca = Column(String(50), nullable=False)
    modelo = Column(String(50), nullable=False)
    placa=Column(String(20), nullable=False)
    ano = Column(Integer, nullable=False)
    valor_diaria = Column(Numeric(10,2), nullable=False)

# ADICIONANDO VEÍCULO
def add_veiculo(ID_veiculo, marca, modelo, ano, placa, valor_diaria):
    novo_Veiculo=Veiculo(ID_veiculo=ID_veiculo, marca=marca, modelo=modelo, placa=placa, ano=ano, valor_diaria=valor_diaria)
    session.add(novo_Veiculo)
    session.commit()
    print(f'Veículo foi adicionado com sucesso!')

# ATUALIZANDO VEÍCULO
def update_veiculo_viaID(ID_veiculo):
    veiculo=session.query(Veiculo).filter_by(ID_veiculo=ID_veiculo).first()
    if veiculo:
        novo_valor=input('Qual o novo valor da diária do veículo? R$')
        nova_placa=str(input('Qual a nova placa do carro? ')).upper()
    #ADICIONANDO NA TABELA O UPDATE
        veiculo.valor_diaria=novo_valor
        veiculo.placa=nova_placa
        session.commit()
        print(f'Informações de veículo atualizadas!\nNovo valor de diária: R${novo_valor:.2f}.\nPlaca nova: {nova_placa}.')

# DELETANDO VEÍCULO
def delete_veiculo_viaID(ID_veiculo,marca, modelo, ano, placa):
    veiculo=session.query(Veiculo).filter_by(ID_veiculo=ID_veiculo).first()
    if veiculo:
        session.delete(veiculo)
        session.commit()
        print(f'Veículo {marca} modelo {modelo}, ano {ano}, placa: {placa} foi excluído do banco com sucesso.')
    else:
        print(f'Veículo digitado não encontrado.')

#LISTANDO CARACTERÉISTICAS DE VEÍCULOS
def listar_veiculos():
    todos_veiculos=session.query(Veiculo).all()
    if todos_veiculos:
        for veiculo in todos_veiculos:
            print(f'ID: {veiculo.ID_veiculo} marca: {veiculo.marca} modelo: {veiculo.modelo} ano: {veiculo.ano} placa: {veiculo.placa} valor da diária: R${veiculo.valor_diaria}.')
    else: 
        print('Veículo não foi encontrado.')

#MENU
opcoes='''==================================================
            Menu de opções:
    1- Adicionar veículo.
    2- Atualizar informações do veículo com ID.
    3- Deletar veículo com ID.
    4- Listar características do veículo.
    5- Atualizar via placa.
    6- Deletar via placa.
    7- Listar via placa. 
    8- Sair.
=================================================='''
#FUNÇÃO PARA GERAR MENU
def menu():
    while True:
        print(opcoes)
        escolha=input('Escolha uma opção: ')
        if escolha =='1':
            marca=input('Marca do veículo: ')
            modelo=input('Modelo do veículo: ')
            ano=int(input('Ano de fabricação do veículo: '))
            placa=str(input('Placa do carro: ')).upper()
            valor_diaria=float(input('Qual o valor da diária deste veículo? R$'))
            add_veiculo(marca, modelo, ano, placa, valor_diaria)
        elif escolha == '2':
            listar_veiculos()
            id= int(input('ID do veículo: '))
            update_veiculo_viaID(id)
        elif escolha == '3':
            listar_veiculos()
            id= int(input('ID do veículo: '))
            delete_veiculo_viaID(id)
        elif escolha == '4':
            listar_veiculos()
        


menu()






