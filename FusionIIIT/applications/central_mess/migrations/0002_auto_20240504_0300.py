# Generated by Django 3.1.5 on 2024-05-04 03:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central_mess', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='payment_date',
            field=models.DateField(default=datetime.date(2024, 5, 4)),
        ),
    ]
