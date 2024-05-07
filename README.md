# Flask API with MongoDB

This is a simple Flask API that interacts with a MongoDB database. The API allows you to perform CRUD (Create, Read, Update, Delete) operations on a table named `mytable`.

## Requirements

- Python 3.10
- Flask
- PyMongo
- Docker (optional)

## Installation

1. Clone the repository:

```
git clone https://github.com/Hallexz/compose.git
```

2. Change to the project directory:

```
cd compose
```

3. Create a virtual environment and activate it:

```
python -m venv venv
source venv/bin/activate
```

4. Install the required packages:

```
pip install -r requirements.txt
```

## Running the API

1. Start the Flask development server:

```
flask run --host=0.0.0.0 --port=8080
```

The API will be accessible at `http://localhost:8080/`.

## Running with Docker

1. Build the Docker image:

```
docker build -t compose .
```

2. Start the Docker containers:

```
docker-compose up -d
```

The API will be accessible at `http://localhost:8080/`.

## API Endpoints

- `GET /`: Retrieve a value from the `mytable` table by providing the `key` as a query parameter.
- `POST /`: Insert a new key-value pair into the `mytable` table. Provide the `key` and `value` in the request body.
- `PUT /`: Update an existing value in the `mytable` table by providing the `key` and the new `value` in the request body.

## Example Usage

### Retrieve a value

```
curl http://localhost:8080?key=my_key
```

### Insert a new key-value pair

```
curl -X POST -d 'key=my_key&value=my_value' http://localhost:8080
```

### Update an existing value

```
curl -X PUT -d 'key=my_key&value=new_value' http://localhost:8080
```

