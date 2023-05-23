from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField
from django.core.validators import MaxValueValidator, MinValueValidator

from datetime import datetime
import pytz

from django.db import models


GENRES = (
    ('adventure', 'Приключения'),
    ('romance', 'Романтика'),
    ('thriller', 'Триллер'),
    ('fantasy', 'Фантастика'),
    ('drama', 'Драма'),
    ('Horror', 'Ужасы'),
)


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name=_('Название фильма'))
    genre = MultiSelectField(choices=GENRES, max_length=120, verbose_name=_('Жанр'))
    age_rate = models.PositiveSmallIntegerField(verbose_name=_('Возрастное ограничение'))
    rating = models.FloatField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name=_('Отзыв')
    )
    is_active = models.BooleanField(default=True, verbose_name=_('Идет в прокате'))
    start_date = models.DateTimeField(verbose_name=_('Начало проката'))
    end_date = models.DateTimeField(verbose_name=_('Конец проката'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _('Фильм')
        verbose_name_plural = _('Фильмы')

    @property
    def set_is_active(self):
        self.is_active = self.start_date <= datetime.now().replace(tzinfo=pytz.UTC) <= self.end_date

    def __str__(self):
        return f"{self.title}"

