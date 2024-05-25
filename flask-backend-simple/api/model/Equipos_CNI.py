import functools
import db
import pymysql

def get_equiposCNI():
    con = db.get_connection()
    cursor = con.cursor(pymysql.cursors.DictCursor)
    try:
        sql="SELECT * FROM Equipos_CNI"
        cursor.execute(sql)
        ret = cursor.fetchall()
        print(ret)
        return ret
    finally:
        con.close()

def get_modelo(id_modelo):
    con = db.get_connection() 
    cursor = con.cursor(pymysql.cursors.DictCursor)
    ret={}
    try:
        sql="SELECT * FROM Equipos_CNI WHERE id = {}".format(id_modelo)
        cursor.execute(sql)
        ret = cursor.fetchone()
        return ret
    finally:
        con.close()

def get_equipo_by_tipo(tipo_equipo):
    con = db.get_connection() 
    cursor = con.cursor(pymysql.cursors.DictCursor)
    ret={}
    try:
        sql="SELECT * FROM Equipos_CNI WHERE name = '{}'".format(tipo_equipo)
        print(sql)
        cursor.execute(sql)
        ret = cursor.fetchone()
        return ret
    finally:
        con.close()

def create_equipoCNI(cantidad, tipo_equipo):
    con = db.get_connection()
    cursor = con.cursor()

    '''company = get_company_by_name(name)
    if company:
        return {"message": "User exists"}'''
    try:
        sql="INSERT INTO Equipos_CNI(cantidad, tipo_equipo) VALUES('{}','{}')".format(cantidad, tipo_equipo)
        print(sql)
        cursor.execute(sql)
        con.commit() # confirmar que guarde en la db los insert, mediante verificacion de cumplimiento de todas las transacciones
        id_org = cursor.lastrowid
        return {"message":"OK", "id": id_org}
    finally:
        con.close()

def update_equipo(cantidad, tipo_equipo, id_modelo):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="UPDATE Equipos_CNI set cantidad='{0}', tipo_equipo='{1}' WHERE id = {2}".format(cantidad, tipo_equipo, id_modelo)
        print(sql)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK"}
    finally:
        con.close()

def delete_company(company_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="DELETE FROM companies WHERE id = {}".format(company_id)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK"}
    finally:
        con.close()