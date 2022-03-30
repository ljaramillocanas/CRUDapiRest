from distutils.log import debug
import MySQLdb
from flask import Flask, jsonify
from config import config
from flask_mysqldb import MySQL


app=Flask(__name__)

conexion = MySQL(app)

@app.route('/cursos')
def listar_cursos():

    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM curso"
        cursor.execute(sql)
        datos = cursor.fetchall()
        cursos= []
        for fila in datos:
            curso ={'codigo':fila[0],'creditos':fila[1],'nombre':fila[2]}
            cursos.append(curso)
        print(datos)
        return jsonify({'cursos':cursos,'Mensaje':"Cursos listados"})

    except Exception as ex:
            return jsonify({'Mensaje':"error"})


def pag_no_encontrada(error):
    return "<h1>LA PAGINA QUE INTENTAS BUSCAR NO EXISTE ! </h1>"

if __name__ == '__main__':
    app.config.from_object('config.DevelopmentConfig')
    app.register_error_handler(404,pag_no_encontrada)
    app.run( )