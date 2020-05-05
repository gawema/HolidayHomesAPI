from django.db import models
from django.contrib.auth.models import User

class House(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(User, related_name='house', on_delete=models.CASCADE)

def __str__(self):
    return self.name