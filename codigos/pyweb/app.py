# IMPORTS 
from flask import Flask, render_template, request, Response
from datetime import datetime

# IMPORTAR a classe Cliente do arquivo entidades.py
from entidades import Cliente

# criado o servidor web (flask)
app = Flask(__name__)
# Flask é a classe
# app é a instancia (objeto)

# http://localhost:5000/
@app.route("/") # caminho da pagina principal
def index():
    return render_template('index.html')

# http://localhost:5000/bomdia
@app.route("/bomdia")  # representa caminho /bomdia
def bomdia():
    return render_template("index.html")

# /cotacao
@app.route("/cotacao")
def cotacao():
    valor = 5.21
    preco = 100
    total = valor * preco
    return render_template(
        "cotacao.html", 
        valor=valor, preco=preco, total=total
        )

# TODO: implementar listar clientes
"""
/listar
def listar():

    dc = ClienteDao()
    clientes = dc.findall

    return render template listar_cliente 

"""

@app.route("/cliente", methods=["POST","GET"])
def cliente():
    # recebe cada input do formulário aqui
    # cria um cliente usando 
    # cliente = Cliente()
    id = int(request.form.get("id"))
    nome = request.form.get("nome")

    cliente = Cliente(id, nome)
    # cliente.cep = cep



    pass

# http://localhost:5000/conversao
@app.route("/conversao", methods=["POST","GET"])
def conversao():
    #(GET) eh o caso quando usuario digita a url no browser
    if request.method == 'GET':
        return render_template("conversao.html")
    else:
        #(POST) eh quando envia o formulario (clica calcular)
        # 4. recebe o valor em dolar preco
        preco = float(request.form.get("preco"))
        
        # 5. calcula o valor
        # TODO: pegar o preco da cotacao em:
        # https://docs.awesomeapi.com.br/api-de-moedas
        valor_reais = preco * 5.24
        # retorna o valor (Resposta)
        return render_template(
            "conversao.html", valor_reais = valor_reais
            )

if __name__ == "__main__":
    app.run(debug=True)
