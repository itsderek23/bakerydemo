# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 08:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('wagtailsearchpromotions', '0002_capitalizeverbose'),
        ('base', '0017_standardpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutpage',
            name='image',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='AboutPage',
        ),
    ]
