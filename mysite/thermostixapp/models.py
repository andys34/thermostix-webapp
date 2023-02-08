from django.db import models
import uuid
from django.db.models import Model


# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=120)

    def __str__(self):
        return self.username


class Thermometer(models.Model):
    assignedUsers = models.ManyToManyField(User)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.id


class Log(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    thermometer = models.ManyToManyField(Thermometer)
    temperature = models.FloatField()
    time = models.DateTimeField()

    def __str__(self):
        return self.id
