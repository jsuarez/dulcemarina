from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from ckeditor.fields import RichTextField

# Create your models here.

class QuienesSomos(models.Model):
    titulo_nosotros = models.CharField(max_length=100)
    #descripcion_nosotros = models.TextField()
    descripcion_nosotros = RichTextField(help_text=u"Redacta una descripcion")
    #imagen_nosotros = models.ImageField(upload_to='media/nosotros')
    imagen_original_nosotros = models.ImageField(upload_to='nosotros', blank=True)
    imagen_nosotros = ImageSpecField(source='imagen_original_nosotros',
                                      #processors=[ResizeToFill(1351, 338)], es como la agarra el navegador!
                                      processors=[ResizeToFill(940, 450)],
                                      format='JPEG',
                                      options={'quality': 100})
    pub_date = models.TimeField(auto_now=True)

    def __unicode__(self):              # __str__ en Python 3
        return self.titulo_nosotros

    class Meta:
        verbose_name_plural = 'Nosotros'