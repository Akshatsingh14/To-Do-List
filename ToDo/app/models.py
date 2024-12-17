from django.db import models

# Create your models here.
class List(models.Model):
    task = models.CharField(max_length=200)

    def __str__(self):
        return self.task

class History(models.Model):
    dtask = models.CharField(max_length=200)
    
    def __str__(self):
        return self.dtask