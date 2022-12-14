# Generated by Django 4.1.3 on 2022-12-08 20:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='guest',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='bookings',
                to=settings.AUTH_USER_MODEL,
                verbose_name='Guest',
            ),
        ),
        migrations.AddField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='bookings',
                to='rooms.room',
                verbose_name='Room',
            ),
        ),
    ]
