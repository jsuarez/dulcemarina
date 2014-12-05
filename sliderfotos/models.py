from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.

class Foto(models.Model):
	nombre_de_imagen = models.CharField(max_length=50)
    #imagen_slider = models.ImageField(upload_to='media/slider')
	imagen_original_slider = models.ImageField(upload_to='slider')
	imagen_slider = ImageSpecField(source='imagen_original_slider',
                                      #processors=[ResizeToFill(1351, 338)], es como la agarra el navegador!
                                      processors=[ResizeToFill(940, 450)],
                                      format='JPEG',
                                      options={'quality': 100})
	pub_date = models.TimeField(auto_now=True)

	def __unicode__(self):              # __str__ en Python 3
		return self.nombre_de_imagen

	class Meta:
		verbose_name_plural = 'Slider de Fotos'