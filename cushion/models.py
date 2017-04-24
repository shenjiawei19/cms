# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class play_info(models.Model):

    date = models.DateField(default=None,null=True)
    cdn_id = models.IntegerField(default=None,null=True)
    type = models.CharField(default=None,max_length=10,null=True)
    nobuffer_pro = models.DecimalField(max_digits=6,decimal_places=2,null=False)
    fluency_pro = models.DecimalField(max_digits=6,decimal_places=2,null=False)
    custom_unusual_pro = models.DecimalField(max_digits=6,decimal_places=2,null=False)
    average_playtime =  models.DecimalField(max_digits=20,decimal_places=2,null=False)
    gt3caton_pro =  models.DecimalField(max_digits=6,decimal_places=2,null=False)
    uv = models.IntegerField(default=None,null=True)
    vv = models.IntegerField(default=None,null=True)

    class Meta:
        app_label = None
        db_table = 'play_info'

class n_info(models.Model):

    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(default=None)
    model = models.CharField(default=None,max_length=50,null=True)
    type = models.CharField(default=None,max_length=50,null=True)
    nobuffer = models.IntegerField(default=0,null=True)
    fluency = models.IntegerField(default=0,null=True)
    unusual =  models.IntegerField(default=0,null=True)
    average =  models.IntegerField(default=0,null=True)
    gt3 = models.IntegerField(default=0,null=True)
    fbuffer = models.IntegerField(default=0,null=True)
    vv = models.IntegerField(default=0,null=True)
    ip = models.CharField(default=None,null=True)

    class Meta:
        app_label = None
        db_table = 'ninfo'