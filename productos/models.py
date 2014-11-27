from django.db import models

# Create your models here.

class Producto(models.Model):
    titulo_producto = models.CharField(max_length=100)
    descripcion_producto = models.TextField(max_length=800)
    imagen_producto = models.ImageField(upload_to='img/productos')
    pub_date = models.TimeField(auto_now=True)
