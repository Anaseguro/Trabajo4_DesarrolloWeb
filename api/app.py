from flask import Flask, request, jsonify
from flask_cors import CORS

from model.Ubicaciones import (
    get_ubicaciones,
    get_ubi_id,
    get_sala,
    create_sala,
    update_sala,
    delete_sala
)

from model.Equipo import (
    get_equipos,
    get_equipo_id,
    get_equipo_marca,
    create_equipo,
    update_equipo,
    delete_equipo
)

from model.users import (
    get_users,
    get_user_id,
    create_user,
    update_user,
    delete_user,
)

app = Flask(_name_)
CORS(app)

#Ubicacion
@app.route('/ubicacion', methods=['GET'])
def list_ubicacion():
    retorno = get_ubicaciones()
    return jsonify(retorno)

@app.route('/ubicacion/<int:ubi_id>', methods=['GET']) 
def get_ubicacion_by_id(ubi_id):
    return jsonify(get_ubi_id(ubi_id))

@app.route('/ubicacion/sala/<ubicacion_name>', methods=['GET'])
def get_ubi_by_name(ubicacion_name):
    return jsonify(get_sala(ubicacion_name)) 

@app.route('/ubicacion', methods=['POST'])
def create_ubi():
    data = request.get_json()
    name = data['name']
    description = data['description']
    paciente_1= data['paciente']
    equipo_1= data['equipos']
    return jsonify(create_sala(name, description,paciente_1,equipo_1))

@app.route('/ubicacion/<int:ubi_id>', methods=['PUT']) 
def update_ubi(ubi_id):
    data = request.get_json()
    name = data['salas']
    description = data['descripcion']
    paciente_1= data['paciente']
    equipo_1= data['equipos']
    return jsonify(update_sala(name, description,paciente_1,equipo_1, ubi_id))

@app.route('/ubicacion/<int:ubi_id>', methods=['DELETE'])
def delete_companies(ubi_id):
    return jsonify(delete_sala(ubi_id))


#Equipos
@app.route('/equipo', methods=['GET'])
def list_equipo():
    retorno = get_equipos()
    return jsonify(retorno)

@app.route('/equipo/<int:equipo_id>', methods=['GET']) 
def get_equipo_by_id(equipo_id):
    return jsonify(get_equipo_id(equipo_id))

@app.route('/equipo/nombre/<equipo_name>', methods=['GET'])
def get_equipo_by_name(equipo_name):
    return jsonify(get_equipo_marca(equipo_name)) 

@app.route('/equipo', methods=['POST'])
def create_equipo():
    data = request.get_json()
    name = data['nombre']
    marca_1 = data['marca']
    description = data['descripcion']
    mant= data['mantenimiento']
    fecha= data['fecha_mant']
    return jsonify(create_equipo(name,marca_1,description,mant,fecha))

@app.route('/equipo/<int:equipo_id>', methods=['PUT']) 
def update_equipo(equipo_id):
    data = request.get_json()
    name = data['nombre']
    marca_1 = data['marca']
    description = data['descripcion']
    mant= data['mantenimiento']
    fecha= data['fecha_mant']
    return jsonify(update_equipo(name,marca_1,description,mant,fecha, equipo_id))

@app.route('/equipo/<int:equipo_id>', methods=['DELETE'])
def delete_equipo(equipo_id):
    return jsonify(delete_equipo(equipo_id))


#users
@app.route('/users', methods=['GET'])
def list_users():
    retorno = get_users()
    return jsonify(retorno)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_users(user_id):
    return jsonify(get_user_id(user_id))

@app.route('/users', methods=['POST'])
def create_users():
    data = request.get_json()
    name = data['nombre']
    lastname = data['apellido']
    sint = data['sintomas']
    ubi = data['ubicacion']
    medic = data['medico']
    equip = data['equipo']
    return jsonify(create_user(name, lastname, sint, ubi, medic, equip))

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_users(user_id):
    data = request.get_json()
    name = data['nombre']
    lastname = data['apellido']
    sint = data['sintomas']
    ubi = data['ubicacion']
    medic = data['medico']
    equip = data['equipo']
    return jsonify(update_user(name, lastname, sint, ubi, medic, equip, user_id))

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_users(user_id):
    return jsonify(delete_user(user_id))
