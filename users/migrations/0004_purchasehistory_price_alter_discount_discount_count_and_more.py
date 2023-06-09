# Generated by Django 4.1.7 on 2023-05-24 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_feedback_user_id_purchasehistory_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasehistory',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Сумма'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='discount',
            name='discount_count',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Сумма бонусов'),
        ),
        migrations.AlterField(
            model_name='purchasehistory',
            name='discount_added',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Сумма дополненных бонусов'),
        ),
        migrations.AlterField(
            model_name='purchasehistory',
            name='discount_used',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Сумма использованных бонусов'),
        ),
    ]
