# flask-restapi(WIP)

## API reference
* Listar Sensores:
    * ``` GET /sensores ```
        * RequestBody : **_none_**
        * ResponseBody:  
            * ``` 
                {
                "id": _id,
                "desc" : "descripción del sensor",
                "tipo_sens" : "tipo del sensor,
                "valor" : valor del sensor
                 }, ...
                 ```
    * ```Returns a JSON (Content-type: application/json) with all the sensors info```
* Ver Sensor:
    * ``` GET /sensores/<int:id> ```
        * RequestBody : **_none_**
        * ResponseBody:  
            * ``` 
                {
                "id": _id,
                "desc" : "descripción del sensor",
                "tipo_sens" : "tipo del sensor,
                "valor" : valor del sensor
                 }
                 ```
    * ```Returns a JSON (Content-type: application/json) the sensor info of a specific sensor```
* Crear Sensor:
    * ``` PUT /sensores/<int:id> ```
        * RequestBody :
         * ``` 
                {
                "id": _id,
                "desc" : "descripción del sensor",
                "tipo_sens" : "tipo del sensor,
                "valor" : valor del sensor
                 }
             ```
        * ResponseBody:  **_none_** 
    * ```Create a new register in the database```

## Getting Started

* Clone (or download) a copy of the repository in your machine
* ???
* Enjoy
### Prerequisites

* [Python](https://www.python.org/)

### Installing

```
cd /api-flask-master
pip install -r requirements.txt
```
### Runing
```
cd /api-flask-master
python ./apy.py
```

## Built With

* [Flask-Restful](https://flask-restful.readthedocs.io/en/latest/) - API extension for Flask
* [Flask](http://flask.pocoo.org/) - The web framework used
 
## Authors

* **Tomás Aprile** - *Initial work* - [Kraloz](https://github.com/Kraloz)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
