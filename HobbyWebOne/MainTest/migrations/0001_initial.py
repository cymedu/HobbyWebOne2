# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-09 02:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Img', models.FileField(upload_to='./static/Imginfo')),
                ('hobby', models.CharField(max_length=7)),
                ('thing', models.CharField(max_length=10)),
                ('brand', models.CharField(max_length=10)),
                ('thingname', models.CharField(max_length=20)),
                ('paymoney', models.IntegerField()),
                ('needmoney', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='useraddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=20)),
                ('hobbytype', models.CharField(max_length=7)),
                ('age', models.IntegerField()),
                ('job', models.CharField(max_length=10)),
                ('family', models.CharField(max_length=10)),
            ],
        ),
    ]
