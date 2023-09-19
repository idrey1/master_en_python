# Importar modulo
import sqlite3

# Conexion
conexion = sqlite3.connect('prebas.db')

# Crear cursor
cursor = conexion.cursor()

# Crear tabla
cursor.execute('CREATE TABLE IF NOT EXISTS productos('
               'id integer primary key autoincrement ,'
               'titulo VARCHAR(255),'
               'descripcion TEXT,'
               'precio int(255))')

# Guardar cambios
conexion.commit()

'''
# Insertar datos
cursor.execute('INSERT INTO productos VALUES(null,\'Primer producto\','
               '\'Descripción de mi producto\',550)')
# Guardar cambios
conexion.commit()
'''
# Borrar registros
cursor.execute('DELETE FROM productos')
conexion.commit()

# Insertar muchos registros
productos = [
    ('Telefono movil','Buen Telefono', 140),
    ('Placa Base','Buena placa', 80),
    ('Tablet 15','Buena tablet', 300),
    ('Ordenador portatil','Buen Portatil', 700),
]

# Ejecutar varias sentencias
cursor.executemany('INSERT INTO productos VALUES (NULL,?,?,?)',productos)
conexion.commit()

# Update
cursor.execute('UPDATE productos SET precio=678 WHERE precio=80')

# Listar datos
cursor.execute('SELECT * FROM productos ')
productos = cursor.fetchall()


for producto in productos:
    print('Id:',producto[0])
    print('Titulo:', producto[1])
    print('Descripción:', producto[2])
    print('Precio:', producto[3])
    print('\n')

# Obtenemos el primer registro de nuestra consulta SELECT
cursor.execute('SELECT * FROM productos')
producto = cursor.fetchone()
print(producto)

# Cerrar conexión
conexion.close()