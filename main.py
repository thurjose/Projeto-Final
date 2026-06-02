from flask import Flask

app = Flask(__name__)

from routes import * 
# aqui eu to importando todas as rotas do arquivo routes.py

if __name__ == "__main__": 
# o if vai ser true quando eu realmente executar esse arquivo (main.py)
    app.run()