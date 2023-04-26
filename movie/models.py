from django.db import models
from djongo import models as djongo_models

STATUS_CHOICES = (
    ('coming-up', 'Coming up'),
    ('starting', 'Starting'),
    ('running', 'Running'),
    ('finished', 'Finished'),
)


class CinemaProgram(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    protagonists = models.CharField(max_length=255, null=True, blank=True)
    poster = models.ImageField(upload_to='posters/')
    start_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    ranking = models.IntegerField(default=0)
