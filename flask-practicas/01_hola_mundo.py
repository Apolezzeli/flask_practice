from flask import Flask #Importamos el módulo de Flask.

app = Flask(__name__)  #Creamos una instancia de WSGI de la clase de Flask, dentro de la variable app.


@app.route("/")  #Utilizamos el decorador @app.route para crear la ruta de acceso al API.
def index():
    return "Hola Mundo"  #Por último, definimos una función que retorna el mensaje ‘Hello World’.


app.run()  # Se encarga de ejecutar el servidor 5000
