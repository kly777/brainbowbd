from django.db import models
# Create your models here.
class Todo(models.Model):
    todo = models.CharField(max_length=200)
    startTime=models.DateTimeField
    endTime=models.DateTimeField
    boxName=models.CharField(max_length=200)
    roundTime=models.IntegerField
class schedule(models.Model):
    title=models.CharField(max_length=200)
    detail=models.CharField(max_length=200)
    startTime=models.DateTimeField
    endTime=models.DateTimeField
    boxName=models.CharField(max_length=200)