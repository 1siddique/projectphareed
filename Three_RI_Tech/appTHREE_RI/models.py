from django.db import models
class feedback(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Rating = models.IntegerField()
    Message = models.TextField(max_length=80)

class user(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Rating = models.IntegerField()
    Message = models.TextField(max_length=80)


class contact(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Mobile_Number = models.IntegerField()
    Message = models.TextField(max_length=80)






# Create your models here.
