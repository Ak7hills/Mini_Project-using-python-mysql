from django.db import models

# Create your models here.
class register(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    course = models.CharField(max_length=200)
