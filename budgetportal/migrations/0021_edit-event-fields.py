# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-13 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("budgetportal", "0020_event_status")]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="notes_url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="province",
            field=models.CharField(
                choices=[
                    (b"Eastern Cape", b"Eastern Cape"),
                    (b"Gauteng", b"Gauteng"),
                    (b"North West", b"North West"),
                    (b"Limpopo", b"Limpopo"),
                    (b"Mpumalanga", b"Mpumalanga"),
                    (b"Western Cape", b"Western Cape"),
                    (b"KwaZulu-Natal", b"KwaZulu-Natal"),
                    (b"Northern Cape", b"Northern Cape"),
                    (b"Free State", b"Free State"),
                ],
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="rsvp_url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="type",
            field=models.CharField(
                choices=[
                    (b"hackathon", b"hackathon"),
                    (b"dataquest", b"dataquest"),
                    (b"cid", b"cid"),
                    (b"gift-dataquest", b"gift-dataquest"),
                ],
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="event", name="url", field=models.URLField(blank=True, null=True)
        ),
        migrations.AlterField(
            model_name="event",
            name="video_url",
            field=models.URLField(blank=True, null=True),
        ),
    ]
