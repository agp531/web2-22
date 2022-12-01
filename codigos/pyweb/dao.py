"""
Dao - Data access object
Implementa a conexao com o
banco de dados.

"""
from database import Database
from entidades import Cliente, Produto

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
            (
                cliente.nome,  
                cliente.cpf, 
                cliente.cep,
                cliente.email, 
            )
        )
        conn.commit()
        conn.close()


    def update(self, cliente):
        """
        Realiza UPDATE do cliente
        """
        conn = Database.get_connection()
        conn.execute(
            f"""
            UPDATE cliente SET nome = ?, cpf = ?, cep = ?, email = ?
            WHERE id = ?
            """,
            (
                cliente.nome,
                cliente.cpf,
                cliente.cep,
                cliente.email,
                cliente.id
            )
        )
        conn.commit()
        conn.close()

    def delete(self, id):
        """
        Remove um cliente de acordo com o id fornecido
        """
        conn = Database.get_connection()
        conn.execute(
            # Query
            # Hard Delete (cuidado!)
            f"""
            DELETE FROM cliente WHERE id = {id}
            """
        )
        conn.commit()
        conn.close()


    def find_all(self):
        conn = Database.get_connection()
        res = conn.execute("""
        SELECT id, nome, cpf, cep, email, data_cadastro FROM cliente
        """
        )
        # executa o SELECT
        results = res.fetchall()
        # results eh um vetor

        # versao 1
        results = [
            { 
                "id": cliente[0], 
                "nome": cliente[1],
                "cpf": cliente[2],
                "cep": cliente[3],
                "email": cliente[4],
                "data_cadastro": cliente[5],
            } for cliente in results]

        conn.close()
        return results


    def get_cliente(self, id):
        conn = Database.get_connection()
        res = conn.execute(f"""
        SELECT id, nome, email, cpf, cep, data_cadastro  FROM cliente WHERE id = {id}
        """
        )
        row = res.fetchone()
        
        # cria um objeto cliente para armazenar resultado do SELECT:
        cliente = Cliente( 
            row[1],
            row[2],
            id = row[0],
            cpf = row[3],
            cep = row[4],             
            data_cadastro = row[5]
        )
        conn.close()
        return cliente

    
