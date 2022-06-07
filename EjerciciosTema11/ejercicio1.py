import sqlite3


def conecta(accion):
    conn = sqlite3.connect('mybasedatos.db')
    if accion == 'on':
        return conn.cursor()
    if accion == 'off':
        conn.commit()
        conn.cursor().close()
        conn.close()


def creaTabla():
    on = conecta('on')
    sql = 'CREATE TABLE alumnos(id INTEGER PRIMARY KEY, Nombre TEXT, Apellido TEXT)'
    on.execute(sql)
    conecta('off')


def crearAlumno(id, nombre, apellido):
    conn = conecta('on')
    sql = f'INSERT INTO alumnos(id, Nombre, Apellido) VALUES({id},"{nombre}","{apellido}")'
    conn.execute(sql)
    conecta('off')


def buscarAlumno(nombre):
    conn = conecta('on')
    sql = f'SELECT * FROM Alumnos WHERE Nombre = "{nombre}"'
    conn.execute(sql)
    datos = conn.fetchall()
    conecta('off')
    return datos


datos_alumnos = [
    (1, 'Pepito', 'Piscinas'),
    (2, 'Pocahontas', 'Ludovico'),
    (3, 'Cenicienta', 'Disney'),
    (4, 'Caperucita', 'Roja'),
    (5, 'Javi', 'Empanadilla'),
    (6, 'Lola', 'Seguro'),
    (7, 'Vicente', 'Noveona'),
    (8, 'Raul', 'Azul')]

creaTabla()

for id, nombre, apellido in datos_alumnos:
    crearAlumno(id, nombre, apellido)

print(buscarAlumno('Raul'))
