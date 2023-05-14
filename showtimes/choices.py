from django.db import models


class PriceAges(models.TextChoices):
    Adult = 'Взрослый'
    Child = 'Детский'
    Student = 'Студенческий'
