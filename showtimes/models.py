import uuid
from django.utils.translation import gettext_lazy as _

from django.db import models

from . import choices
from movies.models import Movie
from cinemas.models import Cinema, Room, Seat
from users.models import User


class Showtime(models.Model):
    id = models.AutoField(primary_key=True)
    movie_id = models.ForeignKey(
        to=Movie,
        on_delete=models.CASCADE,
        related_name='movie_showtimes',
        verbose_name=_('Фильм')
    )
    date = models.DateTimeField(verbose_name=_('Дата'))
    room_id = models.ForeignKey(
        to=Room,
        on_delete=models.CASCADE,
        related_name='room_showtimes',
        verbose_name=_('Зал')
    )
    cinema_id = models.ForeignKey(
        to=Cinema,
        on_delete=models.CASCADE,
        related_name='cinema_showtimes',
        verbose_name=_('Кинотеатр')
    )
    tickets_sold = models.PositiveSmallIntegerField(default=0, verbose_name=_('Количество проданных билетов'))
    price_adult = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=_('Цена взрослого билета'))
    price_child = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=_('Цена детского билета'))
    price_student = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=_('Цена студенческого билета'))
    price_vip = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name=_('Цена VIP билета')
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _('Сеанс')
        verbose_name_plural = _('Сеансы')

    def __str__(self):
        return f"{self.movie_id} - {self.cinema_id}, {self.room_id}"


class Ticket(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    showtime_id = models.ForeignKey(
        to=Showtime,
        on_delete=models.CASCADE,
        related_name='showtime_tickets',
        verbose_name=_('Сеанс')
    )
    seat_id = models.ForeignKey(
        to=Seat,
        on_delete=models.CASCADE,
        related_name='seat_tickets',
        verbose_name=_('Место')
    )
    price_age = models.CharField(
        choices=choices.PriceAges.choices,
        max_length=20,
        verbose_name=_('Ценовой возраст')
    )
    user_id = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='user_tickets',
        verbose_name=_('Пользователь')
    )
    status = models.CharField(
        choices=choices.TicketStatuses.choices,
        default=choices.TicketStatuses.Reserved,
        max_length=50,
        verbose_name=_('Статус')
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _('Билет')
        verbose_name_plural = _('Билеты')
