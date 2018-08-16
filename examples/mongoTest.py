from pymongo import MongoClient
# for pretty print
# from pprint import pprint


def main():
    # Connects with MongoDB
    # client = MongoClient()
    # client = MongoClient('localhost', 27017)
    client = MongoClient('mongodb://localhost:27017/')

    # Selects the database
    # db = client['test1']
    db = client.test1

    # Selects the colletion
    # personas = db['personas']
    personas = db.personas
    # Consults the db and print the result
    print(personas.find_one())
    # print(db.personas.find_one({"nombre": "Tomas"}))


if __name__ == '__main__':
    main()
