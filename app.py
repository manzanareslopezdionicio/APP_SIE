from flask import Flask, render_template

app = Flask(__name__)
"""
@app.route('/')
def principal():
    return render_template('home.html')
"""

@app.route('/')
def login():
    return render_template('login1.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/maestro')
def maestro():
    return render_template('maestro.html')

@app.route('/estudiante')
def estudiante():
    return render_template('estudiante.html')

@app.route('/componente')
def componente():
    return render_template('componente.html')

@app.route('/carrera')
def carrera():
    return render_template('carrera.html')

if __name__ == '__main__':
    app.run(debug=True)