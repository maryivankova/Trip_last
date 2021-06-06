from django.db import models

#import datetime
from django.db import models
from django.utils import timezone

class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length = 128)

    def __str__(self):
        return "object  %s %s" % (self.email, self.name)

    class Meta:
        verbose_name = "object"
        verbose_name_plural = "Objects"
