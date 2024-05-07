from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('db', 27017)
db = client['mydatabase']

@app.route('/', methods=['GET', 'POST', 'PUT'])

def index():
    if request.method == 'GET':
        key = request.args.get('key')
        value = db.mytable.find_one({'_id': key})
        return value
    elif request.method == 'POST':
        key = request.form.get('key')
        value = request.form.get('value')
        db.mytable.insert_one({'_id': key, 'value': value})
        return 'Inserted'
    elif request.method == 'PUT':
        key = request.form.get('key')
        new_value = request.form.get('value')
        db.mytable.update_one({'_id': key}, {'$set': {'value': new_value}})
        return 'Updated'
