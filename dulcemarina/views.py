from django.http import HttpResponse
from django.template import RequestContext, loader

from servicios.models import Servicio
from productos.models import Producto
from ajustes.models import Sitio
from nosotros.models import QuienesSomos
from sliderfotos.models import Foto


def home(request):
    lista_servicios = Servicio.objects.order_by('-pub_date')[:5]
    lista_productos = Producto.objects.order_by('-pub_date')[:5]
    lista_ajustes = Sitio.objects.order_by('-pub_date')[:1]
    lista_nosotros = QuienesSomos.objects.order_by('-pub_date')[:1]
    lista_sliderfotos = Foto.objects.order_by('-pub_date')[:5]
    template = loader.get_template('dulcemarina/index.html')
    context = RequestContext(request, {
        'lista_servicios': lista_servicios,
        'lista_productos': lista_productos,
        'lista_ajustes': lista_ajustes,
        'lista_nosotros': lista_nosotros,
        'lista_sliderfotos': lista_sliderfotos,
    })
    return HttpResponse(template.render(context))