from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

class Articles(models.Model):
    title = models.CharField(max_length=100)
    lab = models.CharField(max_length=50,blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True,null=True)