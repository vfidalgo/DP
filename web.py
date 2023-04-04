from flask import Flask, render_template
import base_datos

app = Flask(__name__)

@app.route('/')
def lista_activos():
    activos = base_datos.obtener_activos()
    return render_template('lista_activos.html', activos=activos)

if __name__ == '__main__':
    app.run(debug=True)
