from flask import Flask, render_template
from datetime import datetime

# Flask é um framework web 
# ele executa na url 
# 127.0.0.1:5000 => localhost:5000

# www.google.com
# www.google.com:80
# www.google.com:8080

# criado o servidor web (flask)
app = Flask(__name__)
# Flask é a classe
# app é a instancia (objeto)

# http://localhost:5000/
@app.route("/") # caminho da pagina principal
def hello():
    agora = datetime.now()
    return f"<h1>Seja bem vindo - {agora}</h1>"

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

if __name__ == "__main__":
    app.run(debug=True)
