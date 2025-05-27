from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from supabase import create_client, Client
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Configuración de Supabase
url: str = app.config['SUPABASE_URL']
key: str = app.config['SUPABASE_KEY']
supabase: Client = create_client(url, key)

TABLE_NAME = 'area'

# Crear área del conocimiento
@app.route('/createarea', methods=['GET', 'POST'])
def create_area():
    if request.method == 'POST':
        # Obtener datos del formulario
        name = request.form['name']

        # Insertar en Supabase
        data, count = supabase.table('area').insert({
            "name": name,
        }).execute()

        flash('Área creada exitosamente!', 'success')
        return redirect(url_for('area'))
    
    return render_template('vistas/area.html')

#consultar área del conocimiento
@app.route('/consultarea')
def consult_area():
    try:
     # Consultar todos los registros de la tabla area
        response = supabase.table(TABLE_NAME).select("*").execute()
        areas = response.data
        
        # Verificar si hay datos
        if not areas:
            flash('No se encontraron áreas registradas', 'info')
            
        return render_template('index.html', areas=areas)
    
    except Exception as e:
        flash(f'Error al consultar las áreas: {str(e)}', 'danger')
        return render_template('index.html', areas=[])

# ruta para manejar la página de inicio
@app.route('/')
def home():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('index.html', user=session['user'])

# Ruta para manejar el registro de usuarios
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name= request.form['name']
        
        try:
            # Registrar usuario en Supabase Auth
            user = supabase.auth.sign_up({
                "email": email,
                "password": password,
                "nombre": name,
            })
            
            # Insertar usuario en la tabla 'users' (opcional)
            response = supabase.table('login').insert({
                "email": email,
                "password": password,
                "nombre": name,
                # Almacenar la contraseña de forma segura
                # No almacenar contraseñas en texto plano en producción
                # Usar Supabase Auth para manejar autenticación
            }).execute()
            
            flash('Registro exitoso. Por favor inicia sesión.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            flash(f'Error en el registro: {str(e)}', 'danger')
    
    return render_template('login1.html')

# Ruta para manejar el inicio de sesión
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        try:
            user = supabase.auth.sign_up({
                "email": email,
                "password": password,
            })
            
            if user:
                session['user'] = {
                    'email': email,
                    'id': user.user.id
                }
                flash('Inicio de sesión exitoso.', 'success')
                return redirect(url_for('home'))
        
        except Exception as e:
            flash(f'Error en el inicio de sesión: {str(e)}', 'error')
    return render_template('login1.html')

# Ruta para manejar el cierre de sesión
@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Has cerrado sesión correctamente.', 'info')
    return redirect(url_for('login'))

# mostrar las vistas de la aplicación
@app.route('/areas')
def mostrar_areas():
    
    response = supabase.table(area).select("*").execute()
    areas = response.data
    return render_template('/vistas/area.html', areas=areas)



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

@app.route("/area")
def area():
    return render_template("/vistas/area.html")

if __name__ == '__main__':
    app.secret_key = app.config['SECRET_KEY']
    app.run(debug=True)