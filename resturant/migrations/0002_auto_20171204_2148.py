# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 16:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('resturant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carousel',
            name='display_content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='carousel',
            name='display_title',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carousel',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='slider_image',
            field=models.ImageField(blank=True, null=True, upload_to='slider/%Y/%m/%d'),
        ),
    ]
