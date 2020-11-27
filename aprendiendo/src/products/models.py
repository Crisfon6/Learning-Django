from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.TextField(max_length=120)
    description = models.DateField()
    price = models.TextField()
    summary = models.TextField(default='this is cool')
