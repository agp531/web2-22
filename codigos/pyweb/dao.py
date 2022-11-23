"""
Dao - Data access object
Implementa a conexao com o
banco de dados.

"""
from database import Database

class ProdutoDao:
    # define cada funcionalidade do CRUD
    # CREATE
    def save(self, produto):
        """cria um novo registro no BD"""
        print("Salvando produto...")
        print(produto.nome, produto.preco)
        # TODO: precisa executar o INSERT...

    # READ
    def find_all():
        """le todos os produtos tabela do BD"""
        # TODO: implementar...
        pass

class ClienteDao:

    def save(self, cliente):
        """
        Realiza o INSERT na tabela cliente
        """
        # obtem uma conexao com o banco:
        conn = Database.get_connection()
        conn.execute(
            f"""
            INSERT INTO cliente (
                nome, cpf, cep, email            
            ) VALUES (?, ?, ?, ?)
            """,
            # tupla () 
            (
                cliente.nome,  
                cliente.cpf, 
                cliente.cep,
                cliente.email, 
            )
        )
        conn.commit()


    def find_all(self):
        print('Buscando clientes no BD...')
        # 
        conn = Database.get_connection()
        res = conn.execute("""
        SELECT * FROM cliente
        """
        )
        print(res.fetchall())


if __name__ == '__main__':
    # TODO: remover este codigo (apenas para teste)
    dc = ClienteDao()
    # dc.find_all()

    from entidades import Cliente

    cliente = Cliente(
        "Karina", 
        "kkkk@gmail.com",
        cep="40000-000",
        cpf="400.000.000-11"
    )
    dc.save(cliente)

    dc.find_all()

