from django.db import models


class PayStatuses(models.TextChoices):
    Paid = 'Оплачено'
    Waiting = 'В ожидании'
    Declined = 'Покупка отменена'
