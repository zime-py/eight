from django.db import models

class Do(models.Model):
    name = models.CharField(max_length=100)
    roll = models.CharField(max_length=100) #ForeignKey('auth.user',on_delete=models.CASCADE,)

    def __str__(self):
        return  self.name

class Did(models.Model):
    result = models.CharField(max_length=100) #ForeignKey('auth.user',on_delete=models.CASCADE,)
    do = models.ForeignKey('Do',on_delete=models.CASCADE,)

    def __str__(self):
        return self.result

class Done(models.Model):
    year = models.CharField(max_length=100) #ForeignKey('auth.user',on_delete=models.CASCADE,)
    did = models.ForeignKey('Did',on_delete=models.CASCADE,)

    def __str__(self):
        return self.year

class Go(models.Model):
    position = models.CharField(max_length=100)
    do = models.ForeignKey('Do',on_delete=models.CASCADE,)
    did = models.ForeignKey('Did',on_delete=models.CASCADE,)
    done = models.ForeignKey('Done',on_delete=models.CASCADE,)

    def __str__(self):
        return self.position
