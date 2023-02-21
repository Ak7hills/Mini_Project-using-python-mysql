from django.db import models

# Create your models here.

class Task(models.Model):
    description=models.CharField(max_length=200,blank=True)
    title=models.CharField(max_length=200,blank=True)
    complete=models.BooleanField(default=False)
    create=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


