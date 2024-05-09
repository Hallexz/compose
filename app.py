from flask import Flask, request, jsonify
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError


app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client['mydatabase']


@app.before_first_request
def create_key():
    key = 'test_key'
    value = 'test_value'
    try:
        db.mytable.insert_one({'_id': key, 'value': value})
    except DuplicateKeyError:
        pass  


@app.teardown_appcontext
def delete_key(exception=None):
    key = 'test_key'
    db.mytable.delete_one({'_id': key})


@app.route('/', methods=['GET'])
def get_index():
    key = request.args.get('key')
    value = db.mytable.find_one({'_id': key})
    if value:
        return jsonify(value), 200
    else:
        return 'No value found for the given key', 404


@app.route('/', methods=['POST'])
def post_index():
    key = request.form.get('key')
    value = request.form.get('value')
    if key is not None:
        db.mytable.update_one({'_id': key}, {'$set': {'value': value}}, upsert=True)
        return jsonify({'message': 'Inserted or updated'}), 201
    else:
        return jsonify({'error': 'Key is missing'}), 400


@app.route('/', methods=['PUT'])
def put_index():
    key = request.form.get('key')
    new_value = request.form.get('value')
    existing_value = db.mytable.find_one({'_id': key})
    if existing_value is not None:
        db.mytable.update_one({'_id': key}, {'$set': {'value': new_value}})
        return 'Updated', 200
    else:
        return 'Key not found', 404


if __name__ == "__main__":
    app.run(debug=True)
