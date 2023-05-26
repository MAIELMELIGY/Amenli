from django.db import models

class Currency(models.Model):
    convert_from = models.CharField(max_length=3)
    convert_to = models.CharField(max_length=3)