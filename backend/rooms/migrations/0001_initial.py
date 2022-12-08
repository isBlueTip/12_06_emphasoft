# Generated by Django 4.1.3 on 2022-12-08 20:23

from decimal import Decimal

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'date_check_in',
                    models.DateField(
                        db_index=True, verbose_name='Check-in date'
                    ),
                ),
                (
                    'date_check_out',
                    models.DateField(
                        db_index=True, verbose_name='Check-out date'
                    ),
                ),
            ],
            options={
                'ordering': ['date_check_in'],
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'number',
                    models.PositiveIntegerField(
                        unique=True, verbose_name='Room number'
                    ),
                ),
                (
                    'name',
                    models.CharField(
                        max_length=64, unique=True, verbose_name='Room name'
                    ),
                ),
                (
                    'price',
                    models.DecimalField(
                        db_index=True,
                        decimal_places=2,
                        max_digits=16,
                        validators=[
                            django.core.validators.MinValueValidator(
                                Decimal('0')
                            )
                        ],
                        verbose_name='Price per night',
                    ),
                ),
                (
                    'capacity',
                    models.PositiveIntegerField(
                        db_index=True, verbose_name='Max number of guests'
                    ),
                ),
            ],
            options={
                'ordering': ['number'],
            },
        ),
    ]
