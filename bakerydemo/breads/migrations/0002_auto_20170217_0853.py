# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 08:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0018_remove_rendition_filter'),
        ('breads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='breadsindexpage',
            name='image',
            field=models.ForeignKey(blank=True, help_text='Location listing image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='breadsindexpage',
            name='introduction',
            field=models.TextField(blank=True, help_text='Text to describe the index page'),
        ),
    ]