from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'secret_key_for_sessions'  # Necesario para gestionar sesiones

# Función para conectar a la base de datos SQLite
def conectar():
    return sqlite3.connect('db/artes_peruanos.db')  # Usamos la base de datos SQLite

# Ruta de Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        correo = request.form["correo"]
        contrasena = request.form["contrasena"]

        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Usuario WHERE correo = ? AND contrasena = ?", (correo, contrasena))
        user = cursor.fetchone()
        conn.close()

        if user:
            session["user_id"] = user[0]  # Guardamos el id del usuario en la sesión
            return redirect(url_for('principal'))  # Redirigimos a la página principal
        else:
            return render_template("login.html", mensaje="Credenciales incorrectas")

    return render_template("login.html")

# Ruta principal (Página principal después de login)
@app.route("/principal")
def principal():
    if "user_id" not in session:
        return redirect(url_for('login'))  # Si no hay sesión, redirigimos a login
    return render_template("principal.html")

# Ruta para registrar una nueva cartera
@app.route("/RegistrarCarteraS", methods=["GET", "POST"])
def registrar_cartera():
    if "user_id" not in session:
        return redirect(url_for('login'))

    # Obtener tipos siempre
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM TipoCartera")
    tipos = cursor.fetchall()
    conn.close()

    if request.method == "POST":
        nombre = request.form["nombre"]
        tipo_id = request.form["tipo_id"]
        precio = request.form["precio"]
        fecha = request.form["fecha"]

        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Cartera (nombre, tipo_id, precio, fecha_registro) VALUES (?, ?, ?, ?)",
                       (nombre, tipo_id, precio, fecha))
        conn.commit()
        conn.close()

        mensaje = "Registro grabado con éxito"
        return render_template("RegistrarCarteraS.html", tipos=tipos, mensaje=mensaje)

    # GET: mostrar el formulario sin mensaje
    return render_template("RegistrarCarteraS.html", tipos=tipos)


# Ruta para consultar carteras
@app.route("/ConsultarCartera")
def consultar_cartera():
    if "user_id" not in session:
        return redirect(url_for('login'))

    tipos = listar_tipos()  # Solo obtenemos los tipos, no las carteras
    return render_template("ConsultarCarteraS.html", tipos=tipos, carteras=None)  # <- Aquí enviamos carteras=None


# Obtener todos los tipos de cartera
def listar_tipos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre FROM TipoCartera")
    tipos = cursor.fetchall()
    conn.close()
    return [{"id": row[0], "nombre": row[1]} for row in tipos]

# Obtener carteras filtradas por tipo_id
def consultar_carteras_por_tipo(tipo_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.id, c.nombre, t.nombre AS tipo, c.precio, strftime('%d/%m/%Y', c.fecha_registro) AS fecha_registro
        FROM Cartera c
        JOIN TipoCartera t ON c.tipo_id = t.id
        WHERE t.id = ?
    """, (tipo_id,))
    carteras = cursor.fetchall()
    conn.close()
    return carteras

@app.route("/BuscarCarteras", methods=["POST"])
def buscar():
    if "user_id" not in session:
        return redirect(url_for('login'))

    tipo_id = request.form["tipo_id"]
    tipos = listar_tipos()
    carteras = consultar_carteras_por_tipo(tipo_id)

    return render_template("ConsultarCarteraS.html", tipos=tipos, carteras=carteras)



# Controlador de error 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error404S.html'), 404


if __name__ == "__main__":
    app.run(debug=True, port=5000)

