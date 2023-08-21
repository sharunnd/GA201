from django.db import models

# Create your models here.

class Post(models.Model):
    username = models.CharField(max_length=30)
    caption = models.CharField(max_length=300)