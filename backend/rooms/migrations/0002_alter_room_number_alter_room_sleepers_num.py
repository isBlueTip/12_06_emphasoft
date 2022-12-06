# Generated by Django 4.1.3 on 2022-12-06 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="number",
            field=models.PositiveIntegerField(verbose_name="Room number"),
        ),
        migrations.AlterField(
            model_name="room",
            name="sleepers_num",
            field=models.PositiveIntegerField(verbose_name="Max number of guests"),
        ),
    ]
