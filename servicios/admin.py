from django.contrib import admin
from servicios.models import Servicio, Imagen

# Register your models here.

class ImagenInline(admin.StackedInline):
    model = Imagen
    extra = 1    # Aqui indicamos la cantidad de "slots" que hay de imagenes, el usuario puede agregar mas si lo necesita

class ServicioAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['titulo_servicio', 'descripcion_servicio']}),
    ]
    inlines = [ImagenInline]
    list_display = ('titulo_servicio',)

admin.site.register(Servicio, ServicioAdmin)
