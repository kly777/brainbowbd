from django.db import models


class Tags(models.Model):
    tagname = models.CharField(max_length=20, unique=True)
    fatherTagId = models.CharField(max_length=20)


class Card(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=8192)
    tags = models.ManyToManyField(to=Tags, null=True, blank=True)
    fatherCardId = models.CharField(max_length=333, null=True, blank=True)
    lastCardId = models.CharField(max_length=333, null=True, blank=True)
    createdTime = models.DateTimeField(auto_now_add=True)
    revisedTime = models.DateTimeField(auto_now=True)


class CardTags(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
