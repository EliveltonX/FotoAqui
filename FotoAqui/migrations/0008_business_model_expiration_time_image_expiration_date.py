# Generated by Django 4.2.1 on 2023-06-26 22:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FotoAqui', '0007_alter_image_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='business_model',
            name='expiration_time',
            field=models.IntegerField(default=15),
        ),
        migrations.AddField(
            model_name='image',
            name='expiration_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]