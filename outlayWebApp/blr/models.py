# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Students(models.Model):
	name = models.CharField(max_length=32)
	fathers_name = models.CharField(max_length=32)
	mob_num = models.CharField(max_length=16)
	reg_num = models.CharField(max_length=16)
	address = models.CharField(max_length=500)
	
