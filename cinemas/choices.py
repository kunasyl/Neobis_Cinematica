from django.db import models


class Cities(models.TextChoices):
    Almaty = 'Алматы'
    Astana = 'Астана'
    Shymkent = 'Шымкент'
    Karaganda = 'Караганды'
