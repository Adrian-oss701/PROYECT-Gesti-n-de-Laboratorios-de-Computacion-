from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from routes.auth import auth
from routes.laboratorio import lab
from routes.usuario import usu
from routes.reserva import res
from routes.incidencia import inc

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "umsa2026"
jwt = JWTManager(app)

app.register_blueprint(auth)
app.register_blueprint(lab)
app.register_blueprint(usu)
app.register_blueprint(res)
app.register_blueprint(inc)

@app.route("/")
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/laboratorios-ver")
def laboratorios_view():
    return render_template("laboratorios.html")

@app.route("/reservas-ver")
def reservas_view():
    return render_template("reservas.html")

@app.route("/incidencias-ver")
def incidencias_view():
    return render_template("incidencias.html")

@app.route("/usuarios-ver")
def usuarios_view():
    return render_template("usuarios.html")

if __name__ == "__main__":
    app.run(debug=True)