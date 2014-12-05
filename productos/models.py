from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from ckeditor.fields import RichTextField

# Create your models here.

class Producto(models.Model):
    titulo_producto = models.CharField(max_length=100)
    #descripcion_producto = models.TextField()
    descripcion_producto = RichTextField(help_text=u"Redacta una descripcion del producto")
    imagen_original_producto = models.ImageField(upload_to='productos')
    imagen_producto = ImageSpecField(source='imagen_original_producto',
                                      #processors=[ResizeToFill(1351, 338)], es como la agarra el navegador!
                                      processors=[ResizeToFill(940, 450)],
                                      format='JPEG',
                                      options={'quality': 100})
    pub_date = models.TimeField(auto_now=True)

    def __unicode__(self):              # __str__ en Python 3
        return self.titulo_producto

    class Meta:
        verbose_name_plural = 'Productos'
