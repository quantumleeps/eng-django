# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 19:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('shortname', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plantdata.Location'),
        ),
    ]
