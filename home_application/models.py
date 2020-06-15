# -*- coding: utf-8 -*-
from django.db import models

class IndexModel(models.Model):
    name = models.TextField(max_length=500)
    year = models.DateField()


