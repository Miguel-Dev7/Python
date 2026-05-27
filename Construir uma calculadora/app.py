from flask import Flask, render_template, request
from calculadora import calcular

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return calcular()
    # Se for GET, renderiza a página limpa, sem as variáveis de resultado
    return render_template("calculadora.html", etapa ='', resultado='')

if __name__ == "__main__":
    app.run(debug=True)
