from django.db import models
from django.contrib.postgres.fields import DateRangeField
from users.models import User
from django.core import validators
from decimal import Decimal


class Room (models.Model):
    number = models.PositiveIntegerField(
        unique=True,
        verbose_name='Room number',
    )
    name = models.CharField(
        unique=True,
        max_length=64,
        verbose_name='Room name',
    )
    price = models.DecimalField(
        max_digits=16,
        decimal_places=2,
        validators=[validators.MinValueValidator(Decimal('0'))],  # TODO is it necessary?
        verbose_name='Price per night',
    )
    capacity = models.PositiveIntegerField(
        verbose_name='Max number of guests',
    )

    def __str__(self):
        return f'{self.number} - {self.name}'


class Booking (models.Model):
    room = models.ForeignKey(
        Room,
        related_name='bookings',
        on_delete=models.CASCADE,
        verbose_name='Room',
    )
    guest = models.ForeignKey(
        User,
        related_name='bookings',
        on_delete=models.CASCADE,
        verbose_name='Guest',
    )
    date_range = DateRangeField(
        verbose_name='Nights range',
    )

    def __str__(self):
        return f'{self.room} - {self.date_range}'
