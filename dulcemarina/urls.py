from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
import os
from django.views import generic
from productos import views
#from contact_form import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'dulcemarina.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^servicios/', include('servicios.urls')),

    url(r'^admin/', include(admin.site.urls)),

	url(r'^deployer/', include('deployer.urls')),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^css/(?P<path>.*)$', 'django.views.static.serve',{'document_root': os.path.join(settings.STATIC_ROOT, 'css')}),
    url(r'^fonts/(?P<path>.*)$', 'django.views.static.serve',{'document_root': os.path.join(settings.STATIC_ROOT, 'fonts')}),
    url(r'^images/(?P<path>.*)$', 'django.views.static.serve',{'document_root': os.path.join(settings.STATIC_ROOT, 'images')}),
    url(r'^js/(?P<path>.*)$', 'django.views.static.serve',{'document_root': os.path.join(settings.STATIC_ROOT, 'js')}),
    url(r'^ckeditor/', include('ckeditor.urls')),
)
# Texto para poner al final del <title> de cada pagina.
admin.site.site_title = u'Administracion - Dulce Marina'

# Texto a poner en los <h1> de todas las paginas.
admin.site.site_header = u'Administrador - Dulce Marina'

# Texto a poner arriba de la pagina de index del admin
admin.site.index_title = u'Panel de control - Dulce Marina'