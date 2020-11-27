from django.db import models

# Create your models here.


class User(models.Model):
    name = models.TextField(blank=False, null=True)
    number = models.FloatField()
    password = models.TextField()
