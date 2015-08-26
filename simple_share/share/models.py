from django.db import models
import os
import datetime
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver
from django.conf import settings

class File(models.Model):

    ip = models.CharField(max_length=15)
    note = models.CharField(max_length=250)
    timestamp = models.DateTimeField(default=datetime.datetime.now)
    path = models.CharField(max_length=255)

    def __str__(self):
        return str(self.path.split(os.path.sep)[-1]) + ', ' + str(self.note) + ', ' + str(self.timestamp)

@receiver(post_delete, sender=File)
def file_delete(sender, instance, **kwargs):
    os.remove(os.path.join(settings.UPLOAD_LOCATION, instance.path))
    os.rmdir(os.path.join(settings.UPLOAD_LOCATION, instance.path.split(os.path.sep)[0]))
