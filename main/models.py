from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=2500)

class Usera(AbstractUser):
    age = models.IntegerField()