from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from ckeditor.fields import RichTextField

# Create your models here.

class Servicio(models.Model):
    titulo_servicio = models.CharField(max_length=100)
    #descripcion_servicio = models.TextField(max_length=800)
    descripcion_servicio = RichTextField(help_text=u"Redacta una descripcion del servicio")
    #imagen_servicio = models.ImageField()#[upload_to=None, height_field=None, width_field=None, max_length=100, **options]
    imagen_original_servicio = models.ImageField(upload_to='servicios')
    imagen_servicio = ImageSpecField(source='imagen_original_servicio',
                                      #processors=[ResizeToFill(1351, 338)], es como la agarra el navegador!
                                      processors=[ResizeToFill(940, 450)],
                                      format='JPEG',
                                      options={'quality': 100})
    pub_date = models.TimeField(auto_now=True)

    def __unicode__(self):              # __str__ en Python 3
        return self.titulo_servicio

    class Meta:
        verbose_name_plural = 'Servicios'

class Imagen(models.Model):
    servicio = models.ForeignKey(Servicio)
    #imagen = models.ImageField(upload_to='media/servicios')
    imagen_original = models.ImageField(upload_to='media/servicios')
    imagen = ImageSpecField(source='imagen_original',
                                      #processors=[ResizeToFill(1351, 338)], es como la agarra el navegador!
                                      processors=[ResizeToFill(940, 450)],
                                      format='JPEG',
                                      options={'quality': 100})

