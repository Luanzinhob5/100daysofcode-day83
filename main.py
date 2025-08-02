from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/projetos")
def projetos():
    return render_template("projetos.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

if __name__ == "__main__":
    app.run(debug=True)