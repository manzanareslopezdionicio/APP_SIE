from flask import Flask, render_template, request, redirect, url_for, flash, session   
from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(url, key)

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'

@app.route('/registrar', methods=['GET','POST'])
def registrar():
    if request.method == 'POST':
        data = request.get_json()
        email = request.form['email']
        password = request.form['password']
        nombre = request.form['nombre']
        
        #Registrar new user
        try:
            respuesta = supabase.from_('login').insert(data).execute()
            
            if respuesta.data:
                flash('Datos insertados correctamente','success')
                return redirect(url_for('inicio'))
            else:
                flash('Error al insetar los datos.', 'error')
                return redirect(url_for('login'))
        except Exception as e:
            return redirect(url_for('registrar'))

@app.route('/')
def login():
    return render_template('login1.html')

@app.route('/inicio')
def inicio():
    return render_template('/inicio.html')
""" if 'user' in session:
        return render_template('/inicio.html', user=session['user'])
    else:
        return redirect(url_for('login'))
"""
    
        

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