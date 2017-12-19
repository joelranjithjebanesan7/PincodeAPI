# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Pincode(models.Model):
    officename = models.TextField()
    pincode = models.IntegerField()
    officetype = models.TextField()
    Deliverystatus = models.TextField()
    regionname = models.TextField()
    circlename = models.TextField()
    taluk = models.TextField()
    
    
    class Meta:
        ordering = ('pincode',)
        
    
    