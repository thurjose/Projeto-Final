from flask import Flask
from flask_livereload import LiveReload

app = Flask(__name__)
LiveReload(app) 
# flask live reload é uma extensao do flask q faz ele atualizar automaticamente o meu arquivo sem eu precisar ficar rodando denovo

from routes import * 
# aqui eu to importando todas as rotas do arquivo routes.py

if __name__ == "__main__": 
# o if vai ser true quando eu realmente executar esse arquivo (main.py)
    app.run()