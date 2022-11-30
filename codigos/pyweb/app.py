from flask import (
    Flask, render_template, request, redirect, url_for, flash
)
from entidades import Cliente, Produto
from dao import ClienteDao, ProdutoDao

app = Flask(__name__)
app.config['SECRET_KEY'] = 'wow1001'


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/reset_db", methods=["GET"])
def reset_db():
    from database import Database
    Database.create_db()
    flash(f'Banco de dados Resetado', 'success')
    return redirect(url_for("cliente_index"))
    

# ==================================
# ROTAS (CLIENTE)
# ==================================

@app.route("/cliente/index", methods=["GET"])
def cliente_index():
    dc = ClienteDao()
    clientes = dc.find_all()
    return render_template("cliente_list.html", clientes=clientes)

@app.route("/cliente/new", methods=["GET"])
def cliente_new():
    return render_template("cliente.html", cliente=None)


@app.route("/cliente/edit", methods=["GET"])
def cliente_edit():
    return "<h1>TODO: implementar</h1>"

# -------
# CRUD
# -------

# CREATE
@app.route("/cliente/create", methods=["POST"])
def cliente_create():
    
    nome = request.form.get("nome")
    cep = request.form.get("cep")
    email = request.form.get("email")
    cpf = request.form.get("cpf")

    cliente = Cliente(nome, email, cep=cep, cpf=cpf)

    dao = ClienteDao()
    dao.save(cliente)

    # retornar feedback para o usuário
    # flash(f'Cliente "{nome}" cadastrado!', 'success')

    return redirect(url_for("cliente_index"))


# READ
@app.route("/cliente/<id>", methods=["GET"])
def cliente_id(id):
    # dc = ClienteDao()
    # cliente = dc.get_cliente(id)
    # return cliente.__dict__   
    return "<h1>TODO: implementar</h1>"


# UPDATE
@app.route("/cliente/update", methods=["POST"])
def cliente_update():
    
    dao = ClienteDao()

    return "<h1>TODO: implementar</h1>"


# DELETE
@app.route("/cliente/delete/", methods=["GET"])
def cliente_delete():
    return "<h1>TODO: implementar</h1>"

# ==================================
# ROTAS (PRODUTO)
# ==================================

@app.route("/produto/index", methods=["GET"])
def produto_index():
    return "<h1>TODO: implementar</h1>"


if __name__ == "__main__":
    app.run(debug=True)
    # option 2 (terminal):
    # flask run
