#from django.contrib.auth.models import User
from django.db import models
class post(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    roll = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " : " +self.city + " : " + self.gender

