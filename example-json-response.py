from flask import Flask
from flask import jsonify

app = Flask(__name__)


# A través de la url devuelvo un json con un mensaje
@app.route("/", methods=['GET'])
def api_hello():

    # diccionario de python
    data = {
        'hello': 'world'
    }

    """ formateo a json, con librería nativa de python
    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')"""

    # formateo a json, con api de flask
    resp = jsonify(data)
    resp.status_code = 200
    # resp.headers['X-SomeHeader'] = 'http://url.com'
    return resp


if __name__ == '__main__':
    app.run(debug=True)
