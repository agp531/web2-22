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
    dc = ClienteDao()
    dc.find_all()