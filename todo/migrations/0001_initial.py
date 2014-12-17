# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
                ('status', models.IntegerField(choices=[(-1, 'Cancelled'), (0, 'To Do'), (1, 'Done')], default=0)),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('owner', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ['-status', 'description'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('description', models.CharField(max_length=250, unique=True)),
            ],
            options={
                'ordering': ['description'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='item',
            name='todo_list',
            field=models.ForeignKey(to='todo.List'),
            preserve_default=True,
        ),
    ]
