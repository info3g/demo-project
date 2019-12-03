from django.db import models

# Create your models here.
class Paras(models.Model):
    para=models.TextField()

class data1(models.Model):
    name=models.CharField(max_length=200)
class data2(models.Model):
    error = models.CharField(max_length=200)

class more(models.Model):
    name = models.TextField()
    age = models.TextField()
    city = models.TextField()