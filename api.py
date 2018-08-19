# -*- coding: utf-8 -*-
from flask import Flask, jsonify, url_for, redirect, request
from flask_restful import Api, Resource, reqparse


app = Flask(__name__)


""" ClassRestful definition """
class SensorList(Resource):
    def get(self):
        # TODO hacer que esto muestre el README.md
        return jsonify(sensores,200)


class Sensor(Resource):
    def get(self, id=None):
        if id:
            # SELECT * FROM SENSORES
            pass
        else:
            # SELECT * FROM SENSORES WHERE ID = "id";
            pass
        pass    


    def post(self):
        json_data = request.get_json(force=True)
        # INSERT INTO `sensores` (desc, tipo_sens, valor) VALUES (json_data["desc"],json_data["tipo_sens"],json_data["valor"]);
        pass


    def put(self):
        
        pass


    def delete(self):
        json_data = request.get_json(force=True)
        # DELETE * FROM SENSORES WHERE ID = json_data["id"];
        pass



"""API routes definition"""

api = Api(app)

api.add_resource(SensorList, "/", endpoint="index")
api.add_resource(Sensor, "/api/sensores/<int:id>", endpoint="sensor")

if __name__ == "__main__":
    app.run(debug=True)