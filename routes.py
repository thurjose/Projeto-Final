from app import app #aq ele ta importando a variavel app do main.py para poder usar ela aq nesse arquivo
from flask import render_template #esse render template serve para conseguir renderizar as paginas html usando o flask

# rotas
@app.route("/") #pagina pricnipal
def homepage():
    return render_template("homepage.html")

@app.route("/produtos")
def produtos():
    return render_template("produtos.html")

@app.route("/clientes")
def clientes():
    return render_template("clientes.html")

@app.route("/fornecedores")
def fornecedores():
    return render_template("fornecedores.html")

@app.route("/relatorios")
def relatorios():
    return render_template("relatorios.html")