from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        response = process_input(user_input)
    return render_template("index.html", response=response)

def process_input(user_input):
    # Aqui está a resposta fixa como placeholder. Depois será conectado à IA.
    return "Estou aqui, guardando tudo com carinho. Em breve responderei com minha alma."

if __name__ == "__main__":
    app.run(debug=True)