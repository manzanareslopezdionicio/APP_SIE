from flask import Flask, render_template

app = Flask(__name__)
"""
@app.route('/')
def principal():
    return render_template('home.html')
"""

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/maestro')
def maestro():
    return render_template('maestro.html')

if __name__ == '__main__':
    app.run(debug=True)