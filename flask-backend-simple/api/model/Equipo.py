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

def get_equipo(idEquipo):
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

def create_equipo(Equipos_CNI_id_modelo, Ubicaciones_idUbicaciones):
    con = db.get_connection()
    cursor = con.cursor()

    '''company = get_company_by_name(name)
    if company:
        return {"message": "User exists"}'''
    try:
        sql="INSERT INTO Equipo(Equipos_CNI_id_modelo, Ubicaciones_idUbicaciones) VALUES('{}','{}')".format(Equipos_CNI_id_modelo, Ubicaciones_idUbicaciones)
        print(sql)
        cursor.execute(sql)
        con.commit() # confirmar que guarde en la db los insert, mediante verificacion de cumplimiento de todas las transacciones
        id_org = cursor.lastrowid
        return {"message":"OK", "id": id_org}
    finally:
        con.close()

def delete_company(idEquipo):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="DELETE FROM Equipo WHERE id = {}".format(idEquipo)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK"}
    finally:
        con.close()