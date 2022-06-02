from django.db import models

# Create your models here.
class Icon(models.Model):
    icon_img = models.CharField(max_length=2000)
    # CharField defaults to 200
    icon_description = models.CharField(max_length=200)
    time_todo = models.CharField(max_length=200)

class List(models.Model):
    list_name = models.CharField(max_length=200)
    list_description = models.CharField(max_length=200)

