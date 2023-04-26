# Movie API

Movie API project which contains post api and get api for cinema program

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install -r requirements.txt
```

## Build using docker

```docker
docker-compose up --build -d
```

## Execute Test cases

```python
python manage.py test
```

## Access swagger documentation

Use the [Swagger docs](https:127.0.0.1:8000) to access API's Swagger documentation.

## API list
### 1. Create a new Thing

### Request

`POST /api/v1/cinema_program`
```
curl --location --request POST '127.0.0.1:8000/api/v1/cinema_program' \
--form 'name="test14"' \
--form 'protagonists="test1, test2, test3"' \
--form 'start_date="2023-01-01"' \
--form 'status="coming-up"' \
--form 'poster=@"/Users/dinnu/Downloads/test_image.jpeg"'
```

### Response

    HTTP/1.1 201 Created
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 201 Created
    Connection: close
    Content-Type: application/json
    Location: /thing/1
    Content-Length: 36

    {"id": 5}

### Get list of Things

### Request

`GET /api/v1/cinema_program/`

    curl --location --request GET '127.0.0.1:8000/api/v1/cinema_program'

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    [{
        "id": 1,
        "name": "test14",
        "protagonists": "test1, test2, test3",
        "poster": "http://127.0.0.1:8001/media/posters/test_image_UTRPBcS.jpeg",
        "start_date": "2023-01-01",
        "status": "coming-up",
        "ranking": 280
    },
    {
        "id": 2,
        "name": "test14",
        "protagonists": "test1, test2, test3",
        "poster": "http://127.0.0.1:8001/media/posters/test_image.jpeg",
        "start_date": "2023-01-01",
        "status": "coming-up",
        "ranking": 260
    }]

### We shouldn't push these values, for your easiness I have added these values in readme file. Create a new .env file in the directory where you can see manage.py file
```
MONGO_URL=mongo:27017/
POSTGRES_HOST=db
POSTGRES_DATABASE=movie_task
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin
```