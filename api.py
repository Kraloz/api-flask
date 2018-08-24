# -*- coding: utf-8 -*-

from flask import Flask, jsonify, url_for, redirect, request

from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy

from settings import DB_URI

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

db = SQLAlchemy(app)


""" Modelo de tabla de BD
"""
class ModelSensor(db.Model):
    __tablename__ = "sensores"
    """ Representación de los campos
    """
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(45), unique=False, nullable=True)
    # tipo_sens = Column(Enum(TipoSensores))
    valor = db.Column(db.Integer, unique=False, nullable=True)

    def as_dict(self):    
        return {"id": self.id, "descripcion": self.descripcion, "valor": self.valor}
       

    def __repr__(self):
        return "<Sensor : {}, {}, {}>".format(self.id, self.descripcion, self.valor)


""" Definition of resource classes: """

class Index(Resource):
    def get(self):
        """ Redirecciona al repositorio original del proyecto """
        
        return redirect("https://github.com/Kraloz/api-flask", code=302)


class SensorList(Resource):
    def get(self):
        """ Returns ALL the sensors from the db """

        lista_sensores = []
        
        # SELECT * FROM SENSORES
        for r in ModelSensor.query.all():
            lista_sensores.append(r.as_dict())

        return jsonify({"sensores": lista_sensores}),200


class Sensor(Resource):
    # FUNCIONA
    def get(self, id=None):
        """ Returns the requested sensor """

        # SELECT * FROM SENSORES WHERE ID = "id";
        sensor = ModelSensor.query.get_or_404(id)

        return jsonify({"sensor": sensor.as_dict()}),200


    def post(self):
        # OK        
        json_data = request.get_json()
        # INSERT INTO `sensores` (descripcion, tipo_sens, valor) VALUES (...);

        sens = ModelSensor(descripcion=json_data["descripcion"], valor=json_data["valor"])
        
        db.session.add(sens)
        db.session.commit()
        # Respuesta: 
        response = jsonify()
        response.status_code = 201
        # Location header: 
        response.headers['Location'] = "/sensores/{}".format(sens.id)
        response.autocorrect_location_header = False
        return response


    # WORKING
    def put(self, id=None):
        """ Updates the "valor" field of the sensor requested """
        json_data = request.get_json()

        sensor = ModelSensor.query.get_or_404(id)
        sensor.valor = json_data["valor"]

        db.session.commit()

        response = jsonify()
        response.status_code = 204

        return response


    # WORKING
    def delete(self, id=None):
        """ Deletes the sensor requested from the db """ 
        
        sensor = ModelSensor.query.get_or_404(id)

        # DELETE * FROM SENSORES WHERE ID = ID;
        db.session.delete(sensor)
        db.session.commit()  

        response = jsonify()
        response.status_code = 204      
        
        return response


"""Definition of resource routes: """

api = Api(app)

api.add_resource(Index, "/api/", endpoint="index")

api.add_resource(SensorList, "/api/sensores/", endpoint="sensores")

api.add_resource(Sensor, "/api/sensores/<int:id>", endpoint="sensor")

api.add_resource(Sensor, "/api/sensores/", endpoint="sensorPost")
api.add_resource(Sensor, "/api/sensores/<int:id>/valor", endpoint="sensorUpdate")
api.add_resource(Sensor, "/api/sensores/<int:id>", endpoint="sensorDelete")


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
