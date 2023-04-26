from bson import ObjectId
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from task_movie_api import settings
from .models import CinemaProgram


@receiver(post_save, sender=CinemaProgram, dispatch_uid="sync_cinema_program_to_mongodb")
def sync_cinema_program_to_mongodb(sender, instance, created, **kwargs):
    collection = settings.mongo_client.movie_db.CinemaProgram
    data = {
        'id': instance.id,
        'name': instance.name,
        'protagonists': instance.protagonists,
        'poster': instance.poster.name,
        'start_date': str(instance.start_date),
        'status': instance.status,
        'ranking': instance.ranking,
    }

    if created:
        collection.insert_one(data)
    else:
        collection.update_one({'id': instance.id}, {'$set': data})


@receiver(pre_delete, sender=CinemaProgram)
def delete_cinema_program_from_mongodb(sender, instance, **kwargs):
    collection = settings.mongo_client.movie_db.CinemaProgram
    collection.delete_one({'id': instance.id})
