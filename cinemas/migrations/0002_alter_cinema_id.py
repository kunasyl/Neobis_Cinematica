# Generated by Django 4.1.7 on 2023-05-14 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinemas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinema',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
