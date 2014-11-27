from django.db import models

# Create your models here.

class Sitio(models.Model):
    titulo_sitio = models.CharField(max_length=100)
    descripcion_sitio = models.TextField(max_length=800)
    mail_sitio = models.EmailField()
    pub_date = models.TimeField(auto_now=True)
