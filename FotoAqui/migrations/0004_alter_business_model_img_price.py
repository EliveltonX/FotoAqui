# Generated by Django 4.2.1 on 2023-06-26 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FotoAqui', '0003_image_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business_model',
            name='img_price',
            field=models.FloatField(default=5.0),
        ),
    ]