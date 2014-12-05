from django.db import models

# Create your models here.

class QuienesSomos(models.Model):
    titulo_nosotros = models.CharField(max_length=100)
    descripcion_nosotros = models.TextField()
    imagen_nosotros = models.ImageField(upload_to='static/img/nosotros')
    pub_date = models.TimeField(auto_now=True)
