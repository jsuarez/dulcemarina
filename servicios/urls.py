from django.conf.urls import patterns, url

from servicios import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)