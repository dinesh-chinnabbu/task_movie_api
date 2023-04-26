from django.conf import settings
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from pymongo import MongoClient

from .models import CinemaProgram


@receiver(post_save, sender=CinemaProgram)
def sync_cinema_program_to_mongodb(sender, instance, created, **kwargs):
    # collection = settings.movie_db.CinemaProgram

    data = {
        'name': instance.name,
        'protagonists': instance.protagonists,
        'poster': instance.poster,
        'start_date': instance.start_date,
        'status': instance.status,
        'ranking': instance.ranking,
    }

    # if created:
    #     collection.insert_one(data)
    # else:
    #     collection.update_one({'_id': instance.id}, {'$set': data})


@receiver(post_delete, sender=CinemaProgram)
def delete_cinema_program_from_mongodb(sender, instance, **kwargs):
    # client = MongoClient('mongodb://localhost:27017/')
    # db = client.mydatabase
    # collection = db.CinemaProgramMongo
    #
    # collection.delete_one({'_id': instance.id})
    pass
