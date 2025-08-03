from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contato")
def web():
    return render_template("web.html")

@app.route("/sobre")
def automacoes():
    return render_template("automacoes.html")

if __name__ == "__main__":
    app.run(debug=True)