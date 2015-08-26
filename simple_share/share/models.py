from django.db import models
import os
import datetime

class File(models.Model):

    ip = models.CharField(max_length=15)
    note = models.CharField(max_length=250)
    timestamp = models.DateTimeField(default=datetime.datetime.now)
    path = models.CharField(max_length=255)

    def __str__(self):
        return str(self.path.split(os.path.sep)[-1]) + ', ' + str(self.note) + ', ' + str(self.timestamp)
