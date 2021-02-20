from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    return "Hola Mundo"


@app.route("/saluda")  # Podemos tener n cantidad de funciones y n cantidad de rutas
def saluda():
    return "Te mando un saludo"


@app.route("/params")  # Podemos recibir parametros dentro de la URL en las rutas agregando ? el nombre de la
                       # variable asignada ("params1") y el parametro que le agregamos (Almendra, por ejemplo)
def params():
    param = request.args.get("params1", "No contiene parametro")
    return "El parametro es: {}".format(param) #http://127.0.0.1:8000/params?params1=Almendra_Polezzeli


if __name__ == '__main__':
    app.run(debug=True, port=8000)
