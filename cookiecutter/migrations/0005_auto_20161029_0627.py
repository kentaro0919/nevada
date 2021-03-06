# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-29 06:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cookiecutter', '0004_auto_20161029_0559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cookiecutter.Category'),
        ),
        migrations.AlterField(
            model_name='cutter',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cookiecutter.Category'),
        ),
        migrations.AlterField(
            model_name='cutter',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='cutter'),
        ),
    ]
