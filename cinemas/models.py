from django.utils.translation import gettext_lazy as _

from django.db import models

from . import choices


class Cinema(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True, verbose_name=_('Название'))
    address = models.CharField(max_length=255, verbose_name=_('Адрес'))
    city = models.CharField(
        choices=choices.Cities.choices,
        max_length=50,
        verbose_name=_('Город')
    )
    schedule = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_('Расписание')
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _('Кинотеатр')
        verbose_name_plural = _('Кинотеатры')


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120, verbose_name=_('Название зала'))
    cinema_id = models.ForeignKey(
        to=Cinema,
        on_delete=models.CASCADE,
        related_name='cinema_rooms',
        verbose_name=_('Кинотеатр')
    )
    place_count = models.PositiveSmallIntegerField(verbose_name=_('Количество мест'))
    row_count = models.PositiveSmallIntegerField(verbose_name=_('Количество рядов'))
    seat_count = models.PositiveSmallIntegerField(verbose_name=_('Количество мест в ряде'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _('Зал')
        verbose_name_plural = _('Залы')


class Seat(models.Model):
    id = models.AutoField(primary_key=True)
    room_id = models.ForeignKey(
        to=Room,
        on_delete=models.CASCADE,
        related_name='room_seats',
        verbose_name=_('Зал')
    )
    row = models.PositiveSmallIntegerField(verbose_name=_('Ряд'))
    seat = models.PositiveSmallIntegerField(verbose_name=_('Номер кресла в ряду'))
    is_vip = models.BooleanField(default=False, verbose_name=_('Вип место'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _('Место')
        verbose_name_plural = _('Места')
