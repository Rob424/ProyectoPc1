import os
from flask import Flask, render_template, request
from db.models import listar_tipos, insertar_cartera, consultar_carteras_por_tipo

app = Flask(__name__)

@app.route("/RegistrarCartera")  # Ruta para la página de registro
def registrar():
    tipos = listar_tipos()  # Obtener tipos de cartera desde la base de datos
    return render_template("RegistrarCartera.html", tipos=tipos)

@app.route("/GrabarCartera", methods=["POST"])  # Ruta para grabar la cartera
def grabar():
    nombre = request.form["nombre"]
    tipo_id = request.form["tipo_id"]
    precio = request.form["precio"]
    fecha = request.form["fecha"]
    insertar_cartera(nombre, tipo_id, precio, fecha)  # Inserta en la base de datos
    tipos = listar_tipos()  # Obtener los tipos actualizados
    return render_template("RegistrarCartera.html", mensaje="Registro grabado con éxito", tipos=tipos)

@app.route("/ConsultarCartera")  # Ruta para consultar carteras
def consultar():
    tipos = listar_tipos()  # Obtener tipos de cartera
    return render_template("ConsultarCartera.html", tipos=tipos)

@app.route("/BuscarCarteras", methods=["POST"])  # Ruta para filtrar carteras por tipo
def buscar():
    tipo_id = request.form["tipo_id"]
    tipos = listar_tipos()  # Obtener tipos de cartera
    carteras = consultar_carteras_por_tipo(tipo_id)  # Consultar las carteras por tipo
    return render_template("ConsultarCartera.html", tipos=tipos, carteras=carteras)

# Controlador de error 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error404.html'), 404

#if __name__ == "__main__":
# app.run(debug=True)  

if __name__ == '__main__':
    if not os.path.exists(app.config ['UPLOAD_FOLDER']):
        os.makedirs(app.config [ 'UPLOAD_FOLDER'])
    app.run(debug=True, host="0.0.0.0", port=os.getenv("PORT", default=5000))
