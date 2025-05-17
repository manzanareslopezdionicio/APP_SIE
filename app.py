from flask import Flask, render_template  # type: ignore
from flask_sqlAlchemy  import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)

#app.config("SQLALCHEMY_DATABASE_URI") = "postgresql://postgres:@db.mhkcnviednvvvosahgoa.supabase.co:5432/postgres"

db.init_app(app)

class SupaUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)

with app.app_context():
    db.create_all()

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
    return render_template('/vistas/carrera.html')

@app.route('/rubrica')
def rubrica():
    return render_template('/vistas/rubrica.html')

@app.route("/grupo")
def grupo():
    return render_template("/vistas/grupo.html")

if __name__ == '__main__':
    app.run(debug=True)