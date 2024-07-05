#
# INPORTANDO FALSK E DADOS REQUISITADOS 
#
from flask import Flask, render_template, request
from lista_filmes import resultado_filmes
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite///livros.sqlite3'

db = SQLAlchemy()
db.init_app(app)

conteudos = []
registros = []
#localhost:5000/
@app.route('/', methods=["GET", "POST"])

def principal():
    
    if request.method == 'POST':
        if request.form.get('conteudo'):
            conteudos.append(request.form.get('conteudo'))
    
    
    return render_template('index.html', conteudos = conteudos)

@app.route('/diario', methods=["GET", "POST"])
def diario():
    
    if request.method == "POST":
        if request.form.get("aluno") and request.form.get("nota"):
            aluno = request.form.get("aluno")
            nota = request.form.get("nota")
            registros.append({'aluno': aluno,
                              'nota': nota})
        
    return render_template('sobre.html', registros = registros)

@app.route('/filmes/<propiedade>')
def lista_fimes(propriedade):
    return render_template('filmes.html', filmes = resultado_filmes(propriedade))

    