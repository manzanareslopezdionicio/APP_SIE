import os
from dotenv import load_dotenv
import psycopg2
from psycopg2 import sql, extras
import bcrypt
from flask import Flask, render_template, request, redirect, url_for, session, flash

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'una_clave_secreta_muy_segura')

def get_db_connection():
    conn = psycopg2.connect(
        dbname=os.getenv('SUPABASE_DB'),
        user=os.getenv('SUPABASE_DB_USER'),
        password=os.getenv('SUPABASE_DB_PASSWORD'),
        host=os.getenv('SUPABASE_DB_HOST'),
        port=os.getenv('SUPABASE_DB_PORT')
    )
    return conn
def create_users_table():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            password VARCHAR(100) NOT NULL,
            fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

create_users_table()

def hash_password(password):
    # Generar un salt y hash la contraseña
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def check_password(hashed_password, user_password):
    # Verificar si la contraseña coincide con el hash almacenado
    return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password.encode('utf-8'))

# ruta para manejar la página de inicio
@app.route('/')
def home():
    if 'user_id' in session:
        return redirect(url_for('login'))
    return render_template('login1.html')

#login de usuario
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        conn = get_db_connection()
        cur = conn.cursor()
        
        try:
            cur.execute("SELECT id, nombre, password FROM usuarios WHERE email = %s", (email,))
            user = cur.fetchone()
            
            if user and check_password(user[2], password):
                session['user_id'] = user[0]
                session['user_name'] = user[1]
                flash('Inicio de sesión exitoso!', 'success')
                return redirect(url_for('users'))
            else:
                flash('Email o contraseña incorrectos', 'danger')
        except Exception as e:
            flash('Error al iniciar sesión: ' + str(e), 'danger')
        finally:
            cur.close()
            conn.close()
    
    return render_template('login1.html')

# Registro de usuario
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        hashed_password = hash_password(password)
        
        conn = get_db_connection()
        cur = conn.cursor()
        
        try:
            cur.execute(
                "INSERT INTO usuarios (nombre, email, password) VALUES (%s, %s, %s)",
                (name, email, hashed_password)
            )
            conn.commit()
            flash('Registro exitoso! Por favor inicia sesión.', 'success')
            return redirect(url_for('login'))
        except psycopg2.IntegrityError:
            flash('El email ya está registrado', 'danger')
        except Exception as e:
            flash('Error al registrar: ' + str(e), 'danger')
        finally:
            cur.close()
            conn.close()
    
    return render_template('login1.html')

#lista de usuarios
@app.route('/users')
def users():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        cur.execute("SELECT id, nombre, email, fecha_registro FROM usuarios ORDER BY fecha_registro DESC")
        users = cur.fetchall()
    except Exception as e:
        flash('Error al obtener usuarios: ' + str(e), 'danger')
        users = []
    finally:
        cur.close()
        conn.close()
    
    return render_template('index.html', users=users)

# Ruta para manejar el cierre de sesión
@app.route('/logout')
def logout():
    session.clear()  # Limpiar la sesión
    flash('Has cerrado sesión correctamente.', 'info')
    return redirect(url_for('login'))

# mostrar las vistas de la aplicación


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
    app.run(debug=True)