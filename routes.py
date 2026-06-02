from main import app #aq ele ta importando a variavel app do main.py para poder usar ela aq nesse arquivo
from flask import render_template #esse render template serve para conseguir renderizar as paginas html usando o flask

# rotas
@app.route("/") #pagina pricnipal
def homepage():
    return render_template("homepage.html")

@app.route("/blog")
def blog():
    return "Meu blog"