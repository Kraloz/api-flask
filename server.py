from flask import Flask
from flask import request
from flask_pymongo import PyMongo
# ------------------------------
# para convertir a json
from flask import jsonify
from flask import abort
from bson import json_util, ObjectId
import json


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'test1'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/test1'

mongo = PyMongo(app)


# GET METHOD -OK-
@app.route('/persona/<nombre>', methods=['GET'])
def persona_get(nombre):
    # a través de la url /pedir/opcion devuelvo un json con el índice = opcion"""
    personas = mongo.db.personas
    resp = personas.find_one({"nombre": nombre})

    # Si no existe, not found
    if resp is None:
        # return not_found()
        abort(404)

    """ Para SERIALIZAR un diccionario que viene de MONGODB y poder convertirlo a JSON
        json.loads(json_util.dumps(DICCIONARIO)) """
    resp_sanitized = json.loads(json_util.dumps(resp))

    resp = jsonify(resp_sanitized)
    resp.status_code = 200

    return resp


# POST METHOD
@app.route('/persona/', methods=['POST'])
def persona_post():
    # TODO implement POST method
    pass


# PATCH METHOD -OK-
@app.route('/persona/<id>/<nombre>', methods=['PATCH'])
def persona_put(id, nombre):
    # TODO implement PATCH method
    personas = mongo.db.personas

    personas.update_one({"_id": ObjectId(id)}, {"$set": {"nombre": nombre}})

    return jsonify({"success": "true"})


# DELETE METHOD
@app.route('/persona', methods=['DELETE'])
def persona_delete():
    # TODO implement DELETE method
    pass


# 404 HANDLER
@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


if __name__ == '__main__':
    app.run(debug=True)
