from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    url('departamento/nueva/$', views.departamento_nueva, name='departamento_nueva'),
    ]


from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.empleado_list, name='list'),
    url(r'^departamento/empleado/listar/$', views.empleado_list, name='empleado_list'),
    url(r'^departamento/empleado$', views.empleado_nuevo, name='empleado_nuevo'),
    url(r'^departamento/empleado/editar/(?P<pk>[0-9]+)$', views.empleado_edit, name='empleado_edit'),
    url(r'^departamento/empleado/detalles/(?P<pk>[0-9]+)$', views.empleado_details, name='empleado_details'),    
    url(r'^departamento/empleado/eliminar/(?P<pk>[0-9]+)$', views.empleado_delete, name='empleado_delete'),    
    url(r'^departamento/departamento/listar/$', views.departamento_list, name='departamento_list'),
    url(r'^departamento/empleado/agregar$', views.departamento_nuevo, name='departamento_nuevo'),
    url(r'^departamento/empleado/editar/(?P<pk>[0-9]+)$', views.departamento_edit, name='departamento_edit'),
    url(r'^departamento/empleado/detalles/(?P<pk>[0-9]+)$', views.departamento_details, name='departamento_details'),
    url(r'^departamento/empleado/eliminar/(?P<pk>[0-9]+)$', views.departamento_delete, name='departamento_delete'),

    ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)