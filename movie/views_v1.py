from datetime import date
from typing import Any

import pymongo
from django.core.files.images import ImageFile
from ninja import NinjaAPI, Form
from ninja.responses import Response
from pydantic import BaseModel, Field, validator

from movie.models import CinemaProgram, STATUS_CHOICES
from task_movie_api import settings
from task_movie_api.settings import MEDIA_URL

api_v1 = NinjaAPI(version='1.0.0')


class CinemaSchema(BaseModel):
    name: str
    protagonists: str
    start_date: date
    status: str = Field(min_length=2, max_length=100)
    poster: Any

    @validator('status')
    def validate_status(cls, value):
        if value not in [status[0] for status in STATUS_CHOICES]:
            raise ValueError('Invalid status')
        return value


@api_v1.post("/cinema_program")
def create(request, cinema: CinemaSchema = Form(...)):
    """
    This function creates a new cinema program by accepting a post request to the '/cinema_program' endpoint.

    Parameters:

    request: The HTTP request object sent to the server.
    cinema: A Pydantic BaseModel that defines the schema for creating a new cinema program.
    Returns:

    A dictionary containing the ID of the created cinema program.
    The function creates a new instance of CinemaProgram model by unpacking the validated data from the given cinema schema.
    If a poster is present in the request, it saves the poster file to the cinema program's 'poster' field.
    The function then saves the cinema program instance to the database and returns the ID of the created cinema program.

    Raises:

    This function may raise exceptions related to validation errors of the cinema schema.
    This function may raise exceptions related to saving the cinema program instance to the database.
    """
    cinema_obj = CinemaProgram.objects.create(**cinema.dict())
    poster = request.FILES.get('poster')
    if poster:
        cinema_obj.poster.save(poster.name, ImageFile(poster))
    cinema_obj.save()
    return Response({'id': cinema_obj.id}, status=201)


@api_v1.get("/cinema_program")
def read(request):
    """
    This function reads all cinema programs from the database and returns them in descending order of their ranking.

    Parameters:

    request: The HTTP request object sent to the server.
    Returns:

    A Response object containing a list of dictionaries, each representing a cinema program. Each dictionary contains the details of the cinema program except for its ID.
    The function reads all the documents from the 'CinemaProgram' collection in the MongoDB database using the 'find' method. It removes the '_id' field from the projection and sorts the documents by their 'ranking' field in descending order using the 'sort' method.
    Finally, the function returns the list of cinema programs in the response.

    Raises:

    This function may raise exceptions related to reading data from the database.
    """
    collection = settings.mongo_client.movie_db.CinemaProgram
    docs = collection.find({}, projection={'_id': 0}).sort('ranking', pymongo.DESCENDING)
    result = []
    for doc in docs:
        if doc['poster']:
            doc['poster'] = f"{request.scheme}://{request.get_host()}{MEDIA_URL}{doc['poster']}"
        result.append(doc)
    return Response(result)
