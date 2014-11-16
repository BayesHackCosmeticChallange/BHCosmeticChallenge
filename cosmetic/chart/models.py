# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Score(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    brand = models.TextField(db_column='Brand', blank=True)  # Field name made lowercase.
    product = models.TextField(db_column='Product', blank=True)  # Field name made lowercase.
    efficancy_long = models.FloatField(blank=True, null=True)
    efficancy_short = models.FloatField(blank=True, null=True)
    lavant = models.FloatField(blank=True, null=True)
    presentation = models.FloatField(blank=True, null=True)
    quality = models.FloatField(blank=True, null=True)
    rincable = models.FloatField(blank=True, null=True)
    smell = models.FloatField(blank=True, null=True)
    texture = models.FloatField(blank=True, null=True)
    cas = models.TextField(db_column='CAS', blank=True)  # Field name made lowercase.
    chemical = models.TextField(db_column='Chemical', blank=True)  # Field name made lowercase.

    class Meta:
        db_table = 'score'


class Toxicity(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    chemical = models.TextField(db_column='Chemical', blank=True)  # Field name made lowercase.
    cas = models.TextField(db_column='CAS', blank=True)  # Field name made lowercase.
    cancer = models.IntegerField(db_column='Cancer', blank=True, null=True)  # Field name made lowercase.
    developmental = models.IntegerField(db_column='Developmental', blank=True, null=True)  # Field name made lowercase.
    female_reproductive = models.IntegerField(db_column='Female_Reproductive', blank=True, null=True)  # Field name made lowercase.
    male_reproductive = models.IntegerField(db_column='Male_Reproductive', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'toxicity'
