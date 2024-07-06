from projeto import app
from flask import render_template, request
from projeto.lista_filmes import resultado_filmes
from projeto.livro import livro

conteudos = []
registros = []
# localhost:5000/
@app.route('/', methods=["GET", "POST"])
def principal():
    if request.method == "POST":
        if request.form.get("conteudo"):
            conteudos.append(request.form.get("conteudo"))
            
    return render_template(
        "index.html",
        conteudos=conteudos
    )

@app.route('/diario', methods=["GET", "POST"])
def diario():
    if request.method == "POST":
        if request.form.get("aluno") and request.form.get("nota"):
            aluno = request.form.get("aluno") 
            nota = request.form.get("nota")
            registros.append(
                {
                    "aluno": aluno,
                    "nota": nota
                }
            )
    return render_template(
        "sobre.html",
        registros=registros  
    )
    
@app.route('/filmes/')
def lista_filmes(propriedade):
    return render_template(
        "filmes.html", 
        filmes=resultado_filmes(propriedade)
    )
    
@app.route('/livros')
def lista_livros():
    return render_template(
        "livros.html", 
        livros=livro.query.all()
    )