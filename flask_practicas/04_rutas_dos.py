from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    return "Hola Mundo"


@app.route("/saluda")  # Podemos tener n cantidad de funciones y n cantidad de rutas
def saluda():
    return "Te mando un saludo"

@app.route("/params/")
@app.route("/params/<name>/")  # Tambien podemos recibir parametros dentro de la URL agregando / y el parametro
def params(name = "valor por default"):
    param = request.args.get("params1", "No contiene parametro")
    return "El parametro es: {}".format(name)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
