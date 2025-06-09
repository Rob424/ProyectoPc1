import sqlite3

# Crear base de datos e inicializar tablas
conn = sqlite3.connect('db/artes_peruanos.db')  # Aquí creamos la base de datos
cursor = conn.cursor()

# Crear tabla TipoCartera
cursor.execute("""
CREATE TABLE IF NOT EXISTS TipoCartera (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
)
""")

# Insertar datos en TipoCartera
tipos = ['Tradicional', 'Selvático', 'Andino', 'Costeño']
for tipo in tipos:
    cursor.execute("INSERT INTO TipoCartera(nombre) VALUES (?)", (tipo,))

# Crear tabla Cartera
cursor.execute("""
CREATE TABLE IF NOT EXISTS Cartera (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    tipo_id INTEGER,
    precio REAL,
    fecha_registro TEXT,
    FOREIGN KEY (tipo_id) REFERENCES TipoCartera(id)
)
""")

# Crear tabla Usuario
cursor.execute("""
CREATE TABLE IF NOT EXISTS Usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    correo TEXT NOT NULL UNIQUE,
    contrasena TEXT NOT NULL,
    rol TEXT NOT NULL CHECK(rol IN ('admin', 'usuario'))
)
""")

# Insertar un usuario predeterminado (opcional)
cursor.execute("""
INSERT OR IGNORE INTO Usuario (nombre, correo, contrasena, rol)
VALUES ('admin', 'admin@unfv.edu.pe', 'admin123', 'admin')
""")

# Guardar cambios y cerrar la conexión
conn.commit()
conn.close()

print("✅ Base de datos y tablas inicializadas correctamente.")
