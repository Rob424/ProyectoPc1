from db.conexion import conectar

def listar_tipos():
    con = conectar()
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT * FROM TipoCartera")
    tipos = cur.fetchall()
    con.close()
    return tipos

def insertar_cartera(nombre, tipo_id, precio, fecha):
    con = conectar()
    cur = con.cursor()
    sql = "INSERT INTO Cartera(nombre, tipo_id, precio, fecha_registro) VALUES (%s, %s, %s, %s)"
    cur.execute(sql, (nombre, tipo_id, precio, fecha))
    con.commit()
    con.close()

def consultar_carteras_por_tipo(tipo_id):
    con = conectar()
    cur = con.cursor(dictionary=True)
    sql = """SELECT c.id, c.nombre, t.nombre as tipo, c.precio, DATE_FORMAT(c.fecha_registro, '%d/%m/%Y') AS fecha_registro 
             FROM Cartera c JOIN TipoCartera t ON c.tipo_id = t.id
             WHERE c.tipo_id = %s"""
    cur.execute(sql, (tipo_id,))
    datos = cur.fetchall()
    con.close()
    return datos
