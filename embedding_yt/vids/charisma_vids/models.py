from django.db import models

# Create your models here.
class VideoLink(models.Model):
    link = models.CharField(max_length=128)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name