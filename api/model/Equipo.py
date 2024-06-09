import functools
import db
import pymysql

def get_equipos():
    con = db.get_connection()
    cursor = con.cursor(pymysql.cursors.DictCursor)
    try:
        sql="SELECT * FROM Equipo"
        cursor.execute(sql)
        ret = cursor.fetchall()
        print(ret)
        return ret
    finally:
        con.close()

def get_equipo_id(idEquipo):
    con = db.get_connection() 
    cursor = con.cursor(pymysql.cursors.DictCursor)
    ret={}
    try:
        sql="SELECT * FROM Equipo WHERE id = {}".format(idEquipo)
        cursor.execute(sql)
        ret = cursor.fetchone()
        return ret
    finally:
        con.close()

def get_equipo_marca(marca):
    con = db.get_connection() 
    cursor = con.cursor(pymysql.cursors.DictCursor)
    ret={}
    try:
        sql="SELECT * FROM Equipo WHERE marca = '{}'".format(marca)
        print(sql)
        cursor.execute(sql)
        ret = cursor.fetchone()
        return ret
    finally:
        con.close()

def create_equipo(nombre, marca, descripcion, mantenimiento, fecha_mant):
    con = db.get_connection()
    cursor = con.cursor()

    '''company = get_company_by_name(name)
    if company:
        return {"message": "User exists"}'''
    try:
        sql="INSERT INTO Equipo(nombre, marca, descripcion, mantenimiento, fecha_mant) VALUES('{}','{}','{}','{}','{}')".format(nombre, marca, descripcion, mantenimiento, fecha_mant)
        print(sql)
        cursor.execute(sql)
        con.commit() # confirmar que guarde en la db los insert, mediante verificacion de cumplimiento de todas las transacciones
        id_org = cursor.lastrowid
        return {"message":"Se ha creado el equipo con el id= ", "id": id_org}
    finally:
        con.close()

def update_equipo(nombre, marca, descripcion, mantenimiento, fecha_mant, id_equipo):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="UPDATE Equipo set nombre='{0}', marca='{1}', descripcion='{2}', mantenimiento='{3}', fecha_mant='{4}' WHERE id = {5}".format(nombre, marca, descripcion, mantenimiento, fecha_mant, id_equipo)
        print(sql)
        cursor.execute(sql)
        con.commit()
        return {"message":"Se ha actualizado la informacion del equipo"}
    finally:
        con.close()

def delete_equipo(idEquipo):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="DELETE FROM Equipo WHERE id = {}".format(idEquipo)
        cursor.execute(sql)
        con.commit()
        return {"message":"Se ha eliminado el equipo"}
    finally:
        con.close()