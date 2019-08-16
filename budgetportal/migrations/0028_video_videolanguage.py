# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-16 12:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budgetportal', '0027_infrastructureprojectpart_gps_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_id', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=510)),
            ],
        ),
        migrations.CreateModel(
            name='VideoLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('youtube_id', models.CharField(blank=True, max_length=255, null=True)),
                ('video', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='budgetportal.Video')),
            ],
        ),
    ]