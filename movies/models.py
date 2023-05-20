from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField
from django.core.validators import MaxValueValidator, MinValueValidator

from django.db import models


GENRES = (
        ('adventure', 'Adventure'),
        ('romance', 'Romance'),
        ('thriller', 'Thriller'),
        ('fantasy', 'Fantasy'),
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

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _('Фильм')
        verbose_name_plural = _('Фильмы')

    def __str__(self):
        return f"{self.title}"
