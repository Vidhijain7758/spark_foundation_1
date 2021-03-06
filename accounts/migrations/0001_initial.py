# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-07-17 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_id', models.IntegerField(max_length=20, unique=True)),
                ('Employee_name', models.CharField(default=0, max_length=20)),
                ('Employee_email', models.EmailField(max_length=30)),
                ('Employee_salary', models.IntegerField(default=0, max_length=40)),
            ],
        ),
    ]
