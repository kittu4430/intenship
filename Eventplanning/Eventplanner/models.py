
from django.db import models

# Create your models here.
class Events(models.Model):
    Event_Name=models.CharField(max_length=100)
    Event_Image=models.ImageField(upload_to='pics')
    Event_Description=models.TextField(max_length=100)
    Event_Cost=models.IntegerField(default=0)

