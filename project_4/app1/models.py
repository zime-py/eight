from django.db import models

class cool(models.Model):
    title=models.TextField()
    roll=models.IntegerField()

    def __str__(self):
        return self.title