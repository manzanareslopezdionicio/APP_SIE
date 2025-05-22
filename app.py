from flask import Flask, render_template, request, redirect, url_for, flash, session   
from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()



app = Flask(__name__)

app.secret_key = os.getenv('FLASK_SECRET_KEY', 'supersecretkey')
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(url, key)


@app.route('/')
def home():
    if 'user_email' in session:
        return render_template('inicio.html', email=session['user_email'])
    return redirect(url_for('login'))

@app.route('/inicio')
def inicio():
    return render_template('/inicio.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print(password)
        try:
            user = supabase.auth.sign_in_with_password({
                "email": email,
                "password": password
            })
            session['user_email']=email
            session['access_token'] = user.session.access_token
            flash('Inicio de sesion exitoso.','success')
            return redirect(url_for('home'))
        except Exception as e:
            flash(f'Error en el inicio de sesion: {str(e)}','danger')
    return render_template('login1.html')  

@app.route('/logout')
def logout():
    session.pop('user_email', None)
    session.pop('access_token', None)
    flash('Has cerrado sesion correctamente.', 'info')
    return redirect(url_for('login'))

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

if __name__ == '__main__':
    app.run(debug=True)