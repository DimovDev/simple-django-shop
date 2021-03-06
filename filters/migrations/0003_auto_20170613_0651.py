# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-13 06:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filters', '0002_auto_20170214_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filtercategory',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation date'),
        ),
        migrations.AlterField(
            model_name='filtercategory',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Modification date'),
        ),
        migrations.AlterField(
            model_name='filterselect',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation date'),
        ),
        migrations.AlterField(
            model_name='filterselect',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Modification date'),
        ),
        migrations.AlterField(
            model_name='productfilter',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation date'),
        ),
        migrations.AlterField(
            model_name='productfilter',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Modification date'),
        ),
    ]
