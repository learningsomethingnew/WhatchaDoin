# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 16:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='column',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards_per_column', to='boards.Column'),
        ),
        migrations.AlterField(
            model_name='cards',
            name='order',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='column',
            name='order',
            field=models.IntegerField(),
        ),
    ]
