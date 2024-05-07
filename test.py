import pytest
from your_flask_app import programs
from flask import json
from unittest.mock import patch
from pymongo import MongoClient
from mongomock import MongoClient as MockedMongoClient

@pytest.fixture
def client():
    programs.config['TESTING'] = True
    with programs.test_client() as client:
        yield client

@patch('pymongo.MongoClient', new=MockedMongoClient)
def test_get(client):
    response = client.get('/', query_string={'key': 'key'})
    assert response.status_code == 200

@patch('pymongo.MongoClient', new=MockedMongoClient)
def test_post(client):
    response = client.post('/', data=json.dumps({'key': 'key', 'value': 'value'}), content_type='application/json')
    assert response.status_code == 200
    assert response.get_data(as_text=True) == 'Inserted'

@patch('pymongo.MongoClient', new=MockedMongoClient)
def test_put(client):
    response = client.put('/', data=json.dumps({'key': 'key', 'value': 'new_value'}), content_type='application/json')
    assert response.status_code == 200
    assert response.get_data(as_text=True) == 'Updated'
