from django.db import models

from django.utils import timezone

class TimeTable(models.Model):
    #url = models.CharField(max_length=250, unique=True)
    title = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    #pictureRest = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, **options)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
   
    class Admin:
        pass