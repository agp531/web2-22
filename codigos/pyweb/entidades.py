from datetime import datetime

"""
CRUD 
   C - create (capacidade de adicionar)
   R - read   (capacidade de obter uma info)
   U - update (capacidade de atualizar)
   D - delete (capacidade de remover/apagar)

1. Precisa representar a entidade no código
   - usa orientação a objetos (classes),
   que permitem a definição dos atributos.
2. Interface que exibir informação 
   (html, formulario, tabelas, ...)
3. Criar o mapeamento das classes com as tabelas
   do banco de dados.
   - SQLite: não precisamos instalar
   - é um arquivo que podemos deixar dentro 
   do projeto.
   - MariaDB (mysql), e SQLite usam uma 
   linguagem chamada SQL
   - SQL permite escrever as Queries
    - INSERT => C (create)
    - SELECT => R (read)
    - UPDATE => U (update)
    - DELETE => D (delete)
"""

class Produto:
    def __init__(self, id, nome, preco, marca=None):
        self.id = id        # 635042
        self.nome = nome    # "Processador AMD Ryzen R5 3600 / Soquete AM4"
        self.preco = preco  # 121.00
        self.marca = marca  # "AMD"

class Cliente:
    def __init__(self, id, nome, cpf=None, cep=None):
        # None == null
        self.id = id
        self.nome = nome
        self.cpf = cpf  # atributo opcional
        self.cep = cep  # atributo opcional
        # finalizem! 
        # telefone, senha, data_nasc, email
    
    # que o cliente diga bom dia:
    def bom_dia(self):
        print(f'Bom dia, meu nome é: {self.nome}')
        if self.cpf:
            print(f'Eu tenho um cpf!! {self.cpf}')

if __name__ == '__main__':
    maria = Cliente(1, 'Maria') # chama o __init__
    joao = Cliente(2, 'Joao')
    print(maria.id, maria.nome)
    print(joao.id, joao.nome)

    maria.bom_dia()
    joao.bom_dia()

    lucia = Cliente(3, 'Lucia', cpf='29292929-11')
    lucia.bom_dia()
    """
    fabio = Cliente(
        4, 
        "Fabio", 
        cpf='3838383',
        email='teste@gmail',
        data_nasc = datetime.now(),
        cep='4444'
    )
    """
    ryzen = Produto(
        635042, 
        "Processador AMD Ryzen R5 3600",
        121.00,
        "AMD"
    )
    # print(ryzen.nome, ryzen.preco)
    from dao import ProdutoDao
    dp = ProdutoDao()
    dp.save(ryzen)
    
