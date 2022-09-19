from django.db import models

# Create your models here.
class SchoolProfile(models.Model):
    schoolname = models.CharField(max_length=100)
    schooladdress = models.CharField(max_length=100)
    contact = models.IntegerField()
    pimage = models.ImageField(upload_to='pimages', blank=True)