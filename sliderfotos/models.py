from django.db import models

# Create your models here.

class Foto(models.Model):
    imagen_slider = models.ImageField(upload_to='static/img/slider')
    pub_date = models.TimeField(auto_now=True)