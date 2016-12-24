from django.db import models
from django.utils import timezone

def resort_path(instance, filename):
    url = instance.place + '/' + filename
    return url
# Create your models here.
# class Room(models.Model):
#     name = models.TextField()
#     label = models.SlugField(unique=True)
#
#     def __str__(self):
#         return self.label

class Messages(models.Model):
    # room = models.ForeignKey(Room, related_name='messages')
    handle = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    def __str__(self):
        if self.handle:
            return self.handle
        else:
            return "No handle"

    @property
    def formatted_timestamp(self):
        return self.timestamp.strftime('%b %-d %-I:%M %p')

    def as_dict(self):
        return {'handle': self.handle, 'message': self.message, 'timestamp': self.formatted_timestamp}

class ResortDocument(models.Model):
    place = models.CharField(max_length=200)
    document = models.FileField(upload_to=resort_path)
