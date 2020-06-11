# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class IndexModel(models.Model):
    text = models.TextField(max_length=500)
