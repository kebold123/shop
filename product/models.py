from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    archived = models.BooleanField(default=False)