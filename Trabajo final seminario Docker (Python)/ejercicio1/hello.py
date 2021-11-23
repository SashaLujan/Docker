from flask import Flask
from pymongo import MongoClient
from random import seed
from random import randint

app = Flask(__name__)
client = MongoClient("mongodb://root:root@mongo:27017/")
db = client.test_database

@app.route("/getnumbers")
def get_numbers():
    numbers = db.numbers
    count = numbers.count_documents({})
    return 'Se agregaron {count} números'.format(count=count)

@app.route("/addrandom")
def add_random():
    random_number = randint(0, 100)
    numbers = db.numbers
    number = {"number": random_number}
    numbers.insert_one(number)
    return 'Agregado {random_number}'.format(random_number=random_number)

if __name__ == '__main__':
	app.run(host="0.0.0.0", debug=True)