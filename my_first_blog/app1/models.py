#from django.db import models

# Create your models here.
from django.db import models

class post(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
def __str__(self):
        return self.name

class most(models.Model):
    country = models.CharField(max_length=100)
    about = models.TextField()

    def __str__(self):
            return self.country
