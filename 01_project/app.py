# imports

from flask import Flask, render_template
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy


# my app

# Crear instancia de la aplicación de Flask
app = Flask(__name__)

# Definicion de una ruta (URL) para la raiz del sitio web
@app.route("/")
def index():
    # Funcion que se ejecuta cuando accedemos a la raiz
    return render_template("index.html")

# Verificar si este archivo se está ejecutando directamente (no importado)
if __name__ in "__main__":
    app.run(debug=True)