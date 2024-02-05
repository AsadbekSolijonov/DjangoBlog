from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to='blog/static/images/')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
