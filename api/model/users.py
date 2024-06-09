import functools
import db
import pymysql

def get_users():
    con = db.get_connection()
    cursor = con.cursor(pymysql.cursors.DictCursor)
    try:
        sql="SELECT * FROM users"
        cursor.execute(sql)
        ret = cursor.fetchall()
        print(ret)
        return ret
    finally:
        con.close()

def get_user_id(user_id):
    con = db.get_connection() 
    cursor = con.cursor(pymysql.cursors.DictCursor)
    ret={}
    try:
        sql="SELECT * FROM users WHERE id = {}".format(user_id)
        cursor.execute(sql)
        ret = cursor.fetchone()
        return ret
    finally:
        con.close()

def create_user(nombre, apellido, sintomas, ubicacion, medico, equipo):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="INSERT INTO users(nombre, apellido, sintomas, ubicacion, medico, equipo) VALUES('{}','{}','{}','{}','{}')".format(nombre, apellido, sintomas, ubicacion, medico, equipo)
        print(sql)
        cursor.execute(sql)
        con.commit()
        id_org = cursor.lastrowid
        return {"message":"Se creo el paciente con el id= ", "id": id_org}
    finally:
        con.close()

def update_user(nombre, apellido, sintomas, ubicacion, medico, equipo, user_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="UPDATE users set nombre='{0}', apellido='{1}', sintomas='{2}', ubicacion='{3}', medico='{4}', equipo='{5}' WHERE id = {6}".format(nombre, apellido, sintomas, ubicacion, medico, equipo, user_id)
        print(sql)
        cursor.execute(sql)
        con.commit()
        return {"message":"Se actualizo el paciente"}
    finally:
        con.close()

def delete_user(user_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="DELETE FROM users WHERE id = {}".format(user_id)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK"}
    finally:
        con.close()
