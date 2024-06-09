import functools
import db
import pymysql

def get_ubicaciones():
    con = db.get_connection()
    cursor = con.cursor(pymysql.cursors.DictCursor)
    try:
        sql="SELECT * FROM Ubicaciones"
        cursor.execute(sql)
        ret = cursor.fetchall()
        print(ret)
        return ret
    finally:
        con.close()

def get_ubi_id(id_modelo):
    con = db.get_connection() 
    cursor = con.cursor(pymysql.cursors.DictCursor)
    ret={}
    try:
        sql="SELECT * FROM Ubicaciones WHERE id = {}".format(id_modelo)
        cursor.execute(sql)
        ret = cursor.fetchone()
        return ret
    finally:
        con.close()

def get_sala(nombre_sala):
    con = db.get_connection() 
    cursor = con.cursor(pymysql.cursors.DictCursor)
    ret={}
    try:
        sql="SELECT * FROM Ubicaciones WHERE sala = '{}'".format(nombre_sala)
        print(sql)
        cursor.execute(sql)
        ret = cursor.fetchone()
        return ret
    finally:
        con.close()

def create_sala(sala, descripcion, paciente, equipos):
    con = db.get_connection()
    cursor = con.cursor()

    '''company = get_company_by_name(name)
    if company:
        return {"message": "User exists"}'''
    try:
        sql="INSERT INTO Ubicaciones(sala, descripcion, paciente, equipos) VALUES('{}','{}','{}','{}')".format(sala, descripcion, paciente, equipos)
        print(sql)
        cursor.execute(sql)
        con.commit() # confirmar que guarde en la db los insert, mediante verificacion de cumplimiento de todas las transacciones
        id_org = cursor.lastrowid
        return {"message":"Se ha creado la sala con el id= ", "id": id_org}
    finally:
        con.close()

def update_sala(sala, descripcion, paciente, equipos, id_sala):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="UPDATE Ubicaciones set sala='{0}', descripcion='{1}', paciente='{2}', equipos='{3}' WHERE id = {4}".format(sala, descripcion, paciente, equipos, id_sala)
        print(sql)
        cursor.execute(sql)
        con.commit()
        return {"message":"Se ha actualizado la informacion de la sala"}
    finally:
        con.close()

def delete_sala(sala_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="DELETE FROM Ubicaciones WHERE id = {}".format(sala_id)
        cursor.execute(sql)
        con.commit()
        return {"message":"Se ha borrado la sala del sistema"}
    finally:
        con.close()