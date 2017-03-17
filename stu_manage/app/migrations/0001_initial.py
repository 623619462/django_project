# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('uid', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=38, null=True, blank=True)),
                ('stu_id', models.CharField(max_length=20, null=True, blank=True)),
                ('password', models.CharField(max_length=32, null=True, blank=True)),
                ('class_field', models.CharField(max_length=15, null=True, db_column='class', blank=True)),
                ('usedname', models.CharField(max_length=30, null=True, db_column='usedName', blank=True)),
                ('major', models.CharField(max_length=20, null=True, blank=True)),
                ('id', models.CharField(max_length=30, null=True, blank=True)),
                ('gender', models.CharField(max_length=30, null=True, blank=True)),
                ('birth', models.CharField(max_length=30, null=True, blank=True)),
                ('nation', models.CharField(max_length=30, null=True, blank=True)),
                ('polity', models.CharField(max_length=30, null=True, blank=True)),
                ('nationality', models.CharField(max_length=30, null=True, blank=True)),
                ('province', models.CharField(max_length=30, null=True, blank=True)),
                ('nativeplace', models.CharField(max_length=30, null=True, db_column='nativePlace', blank=True)),
                ('stutypeb', models.CharField(max_length=30, null=True, db_column='stuTypeb', blank=True)),
                ('stutypex', models.CharField(max_length=30, null=True, db_column='stuTypex', blank=True)),
                ('loan', models.CharField(max_length=30, null=True, blank=True)),
                ('domplace', models.CharField(max_length=30, null=True, db_column='domPlace', blank=True)),
                ('dommove', models.CharField(max_length=30, null=True, db_column='domMove', blank=True)),
                ('domplacenew', models.CharField(max_length=30, null=True, db_column='domPlaceNew', blank=True)),
                ('registplace', models.CharField(max_length=30, null=True, db_column='registPlace', blank=True)),
                ('highschool', models.CharField(max_length=30, null=True, db_column='highSchool', blank=True)),
                ('email', models.CharField(max_length=30, null=True, blank=True)),
                ('qq', models.CharField(max_length=30, null=True, blank=True)),
                ('phone', models.CharField(max_length=30, null=True, blank=True)),
                ('address', models.CharField(max_length=30, null=True, blank=True)),
                ('postcode', models.CharField(max_length=30, null=True, blank=True)),
                ('homephone', models.CharField(max_length=30, null=True, db_column='homePhone', blank=True)),
                ('faname', models.CharField(max_length=30, null=True, db_column='faName', blank=True)),
                ('faworkunit', models.CharField(max_length=30, null=True, db_column='faWorkUnit', blank=True)),
                ('fajob', models.CharField(max_length=30, null=True, db_column='faJob', blank=True)),
                ('faphone', models.CharField(max_length=30, null=True, db_column='faPhone', blank=True)),
                ('maname', models.CharField(max_length=30, null=True, db_column='maName', blank=True)),
                ('maworkunit', models.CharField(max_length=30, null=True, db_column='maWorkUnit', blank=True)),
                ('majob', models.CharField(max_length=30, null=True, db_column='maJob', blank=True)),
                ('maphone', models.CharField(max_length=30, null=True, db_column='maPhone', blank=True)),
                ('othermember', models.CharField(max_length=30, null=True, db_column='otherMember', blank=True)),
                ('otherrelation', models.CharField(max_length=30, null=True, db_column='otherRelation', blank=True)),
                ('otherworkunit', models.CharField(max_length=30, null=True, db_column='otherWorkUnit', blank=True)),
                ('otherjob', models.CharField(max_length=30, null=True, db_column='otherJob', blank=True)),
                ('otherphone', models.CharField(max_length=30, null=True, db_column='otherPhone', blank=True)),
                ('campus', models.CharField(max_length=30, null=True, blank=True)),
                ('buiding', models.CharField(max_length=30, null=True, blank=True)),
                ('room', models.CharField(max_length=30, null=True, blank=True)),
                ('grade', models.TextField(null=True, blank=True)),
                ('roll', models.CharField(max_length=30, null=True, blank=True)),
                ('stipend', models.TextField(null=True, blank=True)),
                ('scholarship', models.TextField(null=True, blank=True)),
                ('honour', models.TextField(null=True, blank=True)),
                ('leader', models.TextField(null=True, blank=True)),
                ('abroad', models.TextField(null=True, blank=True)),
                ('academic', models.TextField(null=True, blank=True)),
                ('practice', models.TextField(null=True, blank=True)),
                ('talk', models.TextField(null=True, blank=True)),
                ('remark', models.TextField(null=True, blank=True)),
                ('career', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'information',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Power',
            fields=[
                ('pwid', models.AutoField(serialize=False, primary_key=True)),
                ('uid', models.IntegerField()),
                ('uname', models.CharField(max_length=20)),
                ('rname', models.CharField(max_length=32)),
                ('status', models.IntegerField()),
                ('gid', models.IntegerField()),
            ],
            options={
                'db_table': 'power',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('stu_id', models.CharField(max_length=13)),
                ('password', models.CharField(max_length=32)),
                ('class_field', models.IntegerField(db_column='class')),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='files',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('files', models.FileField(upload_to='uploads')),
            ],
        ),
    ]
