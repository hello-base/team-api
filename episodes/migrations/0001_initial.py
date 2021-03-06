# Generated by Django 2.0 on 2018-01-07 00:48

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('number', models.PositiveSmallIntegerField()),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
