from django.db import models

# Create your models here.

class Sitio(models.Model):
    titulo_sitio = models.CharField(max_length=65)
    descripcion_sitio = models.TextField(max_length=156)
    mail_sitio = models.EmailField()
    pub_date = models.TimeField(auto_now=True)

    def __unicode__(self):              # __str__ en Python 3
        return self.titulo_sitio

    class Meta:
        verbose_name_plural = 'Ajustes Generales'
