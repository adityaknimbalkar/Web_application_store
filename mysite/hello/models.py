from distutils.command.upload import upload
from unicodedata import name
from django.db import models
from django.forms import CharField

# Create your models here.


class Contact(models.Model):
    Email = models.CharField(max_length=122)
    Name = models.CharField(max_length=222)


class Webstore(models.Model):
    App_id = models.AutoField
    App_name = models.CharField(max_length=120)
    App_category = models.CharField(max_length=50)
    App_size = models.IntegerField()
    App_info = models.CharField(max_length=500)
    App_pub_date = models.DateField()
    App_image = models.ImageField(upload_to="static/images")
