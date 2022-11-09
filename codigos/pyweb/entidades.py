from datetime import datetime


class Produto:
    # TODO: precisa implementar futuramente
    pass

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

    fabio = Cliente(
        4, 
        "Fabio", 
        cpf='3838383',
        email='teste@gmail',
        data_nasc = datetime.now(),
        cep='4444'
    )