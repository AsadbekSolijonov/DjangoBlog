from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
