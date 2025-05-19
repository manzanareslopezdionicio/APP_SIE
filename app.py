from flask import Flask, render_template, request, redirect, url_for, flash, session   # type: ignore
from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(url, key)

app = Flask(__name__)

@app.rout('/registrar', methods=['GET','POST'])
def registrar():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        respuesta = supabase.auth.sign_up({'email':email, 'password':password})
        if respuesta.get('error'):
            flash('Error al registrar:'+ respuesta['error']['message'],'danger')
        else:
            flash('Registro exitoso. Por favor inicia sesión.', 'success')
            return redirect(url_for('login'))
    return render_template(url_for('login.html'))
@app.route('/')
def login():
    return render_template('login1.html')

@app.route('/inicio')
def inicio():
    return render_template('/inicio.html')

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
    return render_template('/vistas/carrera.html')

@app.route('/rubrica')
def rubrica():
    return render_template('/vistas/rubrica.html')

@app.route("/grupo")
def grupo():
    return render_template("/vistas/grupo.html")

@app.route('/logout')
def logout():
    session.clear()
    flash('Has cerrado sesión', 'info')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)