#Importando Librerias
from flask import Flask, render_template
from flask import request

app = Flask(__name__)

#Ruta de inicio/Index
@app.route('/')
def home():
    return render_template('home.html')

#Ruta para el formulario que evalua el número mayor
@app.route('/mayor')
def mayor():
    return render_template('mayor.html')

#Ruta para la reseña historica de San Miguel
@app.route('/sanmiguel')
def sanmiguel():
    return render_template('sm.html')

#Pasando diccionario con argumentos
@app.route('/enlace')
def enlace():
    dic = [
        {"url": "https://ugb.instructure.com", "texto": "Canvas UGB"},
        {"url": "https://estudiantes.ugb.edu.sv", "texto": "Portal Estudiante"},
        {"url": "https://www.ugb.edu.sv", "texto": "Sitio UGB"},
        {"url": "https://github.com", "texto": "GitHub"},
        {"url": "https://app.diagrams.net/", "texto": "Draw Io"},
        {"url": "https://es.wikipedia.org", "texto": "Wikipedia"},
        {"url": "https://www.freepik.es", "texto": "Freepik"},
        {"url": "https://www.powtoon.com", "texto": "Powtoon"},
        {"url": "https://logic.ly/demo/", "texto": "Logic.ly"},
        {"url": "https://htmlcolorcodes.com/es/", "texto": "Códigos de color Hex."},
        {"url": "https://getbootstrap.com/", "texto": "Bootstrap"},
        {"url": "https://biblioteca.ugb.edu.sv/", "texto": "Biblioteca UGB"},]

    return render_template('enlace.html', dic=dic)

#Para definir el número mayor
@app.route('/contacto', methods=["POST"])
def resultado():
    n1 = int(request.form.get("n1"))
    n2 = int(request.form.get("n2"))
    mayor = 0
    text = ''
    if n1 == n2:
        mayor = n1
        text = "Ambos números han sido iguales -> "
    if n1 > n2:
        mayor = n1
        text = "El número mayor ha sido: "
    elif n2 > n1:
        mayor = n2
        text = "El número mayor ha sido: "

    return render_template('mayor.html', mayor=mayor, text=text)


#Automatizando la subida de cambios al servidor local
if __name__ == '__main__':
    app.run(debug=True)

