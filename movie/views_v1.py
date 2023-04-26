from typing import Any

from django.core.files.images import ImageFile
from datetime import date

from ninja import Schema
from ninja import NinjaAPI, Form, Field
from ninja.errors import ValidationError
from pydantic import validator
from pydantic import BaseModel, Field, validator
from datetime import date

from movie.models import CinemaProgram, STATUS_CHOICES

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
    cinema_obj = CinemaProgram.objects.create(**cinema.dict())
    poster = request.FILES.get('poster')
    if poster:
        cinema_obj.poster.save(poster.name, ImageFile(poster))
    cinema_obj.save()
    return {'id': cinema_obj.id}
