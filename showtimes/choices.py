from django.db import models


class PriceAges(models.TextChoices):
    Adult = 'Взрослый'
    Child = 'Детский'
    Student = 'Студенческий'
    Vip = 'Вип'


class TicketStatuses(models.TextChoices):
    Reserved = 'Бронь'
    Bought = 'Куплено'
    # Returned = 'Возвращено'
