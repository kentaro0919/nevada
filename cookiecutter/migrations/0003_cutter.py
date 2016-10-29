# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-29 05:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cookiecutter', '0002_auto_20161029_0509'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cutter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='cutter')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('url_in_seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookiecutter.Url_in_Seller')),
            ],
        ),
    ]
