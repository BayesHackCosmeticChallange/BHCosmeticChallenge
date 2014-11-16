# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('brand', models.TextField(db_column='Brand', blank=True)),
                ('product', models.TextField(db_column='Product', blank=True)),
                ('efficancy_long', models.FloatField(null=True, blank=True)),
                ('efficancy_short', models.FloatField(null=True, blank=True)),
                ('lavant', models.FloatField(null=True, blank=True)),
                ('presentation', models.FloatField(null=True, blank=True)),
                ('quality', models.FloatField(null=True, blank=True)),
                ('rincable', models.FloatField(null=True, blank=True)),
                ('smell', models.FloatField(null=True, blank=True)),
                ('texture', models.FloatField(null=True, blank=True)),
                ('cas', models.TextField(db_column='CAS', blank=True)),
                ('chemical', models.TextField(db_column='Chemical', blank=True)),
            ],
            options={
                'db_table': 'score',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Toxicity',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('chemical', models.TextField(db_column='Chemical', blank=True)),
                ('cas', models.TextField(db_column='CAS', blank=True)),
                ('cancer', models.IntegerField(null=True, db_column='Cancer', blank=True)),
                ('developmental', models.IntegerField(null=True, db_column='Developmental', blank=True)),
                ('female_reproductive', models.IntegerField(null=True, db_column='Female_Reproductive', blank=True)),
                ('male_reproductive', models.IntegerField(null=True, db_column='Male_Reproductive', blank=True)),
            ],
            options={
                'db_table': 'toxicity',
            },
            bases=(models.Model,),
        ),
    ]
