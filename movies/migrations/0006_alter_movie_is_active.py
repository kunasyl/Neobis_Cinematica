# Generated by Django 4.1.7 on 2023-05-23 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_movie_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Идет в прокате'),
        ),
    ]
