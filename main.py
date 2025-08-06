from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projetos.db'
db = SQLAlchemy(app)

#Modelo da tabela
class Projeto(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    titulo: Mapped[str] = mapped_column(String(30), nullable=False)
    descricao: Mapped[str] = mapped_column(String(100), nullable=False)
    imagem: Mapped[str] = mapped_column(String, nullable=False)
    link_github: Mapped[str] = mapped_column(String, nullable=False)
    conteudo: Mapped[str] = mapped_column(String(1000), nullable=False)

    def __repr__(self):
        return f'<Projeto {self.titulo}>'


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/automacoes")
def automacoes():
    projetos_automacao = db.session.execute(db.select(Projeto).order_by(Projeto.titulo)).scalars().all()
    return render_template("projetos.html", projetos=projetos_automacao)

if __name__ == "__main__":
    app.run(debug=True)