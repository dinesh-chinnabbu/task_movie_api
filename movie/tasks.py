from celery import shared_task

from movie.models import CinemaProgram


@shared_task(name="increase_movie_ranks")
def increase_movie_ranks():
    cinema_obj = CinemaProgram.objects.filter(status__in=['coming-up', 'starting'])
    for cinema in cinema_obj:
        cinema.ranking += 10
        cinema.save()

