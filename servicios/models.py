from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo_servicio = models.CharField(max_length=100)
    descripcion_servicio = models.TextField(max_length=800)
    imagen_servicio = models.ImageField()#[upload_to=None, height_field=None, width_field=None, max_length=100, **options]
    pub_date = models.TimeField(auto_now=True)

class Imagen(models.Model):
    servicio = models.ForeignKey(Servicio)
    imagen = models.ImageField(upload_to='static/img/servicios')

