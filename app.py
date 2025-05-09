from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/login')
def login():
    return render_template('login1.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/maestro')
def maestro():
    return render_template('/vistas/maestro.html')

@app.route('/estudiante')
def estudiante():
    return render_template('/vistas/estudiante.html')

@app.route('/componente')
def componente():
    return render_template('/vistas/componente.html')

@app.route('/carrera')
def carrera():
    return render_template('carrera.html')

@app.route('/rubricaNivel')
def rubricaNivel():
    return render_template('/vistas/rubricaNivel.html')

@app.route("/grupo")
def grupo():
    return render_template("/vistas/grupo.html")

if __name__ == '__main__':
    app.run(debug=True)