from django.db import models
import datetime

class File(models.Model):

    ip = models.CharField(max_length=15)
    note = models.CharField(max_length=250)
    timestamp = models.DateTimeField(default=datetime.datetime.now)
    path = models.CharField(max_length=255)
