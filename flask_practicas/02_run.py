from flask import Flask #Importamos el módulo de Flask.

app = Flask(__name__)  #Creamos una instancia de WSGI de la clase de Flask, dentro de la variable app.

@app.route("/")  #Utilizamos el decorador @app.route para crear la ruta de acceso al API.
def index():
    return "Cambios"  #Por último, definimos una función que retorna el mensaje ‘Cambios’.

if __name__ == '__main__':
    app.run(debug = True, port = 8000) #Por patametro se puede modificar el puerto que necesitemos.
                                       # El modo debug on, hace que los cambios que vaya realizando sean escuchados
                                       # por el sertvidor
