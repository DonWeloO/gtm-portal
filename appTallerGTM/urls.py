from django.urls import path, include
from django.conf import settings # new
from django.conf.urls.static import static
from .views import home, home2, registro, ingreso, agregarcliente, exito, addVehiculo, clienteHome, diagnostico, \
     exitovehiculo, exitosol, listadovehiculo, listadosolicitud, perfilcliente, exitoactu, editarVeCli, search, exitoreserva

urlpatterns = [
    path('', home2,name='home'),
    path('home/exito/', exito, name='exito'),
    path('home/listadovehiculo/', listadovehiculo, name='listadovehiculo'),
    path('home/listadosolicitud/', listadosolicitud, name='listadosolicitud'),
    path('home/perfilcliente/', perfilcliente, name='perfilcliente'),
    path('home/editarvecli/<str:pk>', editarVeCli, name='editarvecli'),
    path('home/exitovehiculo/', exitovehiculo, name='exitovehiculo'),
    path('home/exitoreserva/', exitoreserva, name='exitoreserva'),
    path('home/exitosol/', exitosol, name='exitosol'),
    path('home/exitoactu/', exitoactu, name='exitoactu'),
    path('home/registro/', registro, name='registro'),
    path('home/ingreso/', ingreso, name='ingreso'),
    path('home/agregar-cliente/', agregarcliente, name='agregar-cliente'),
    path('home/agregar/Vehiculo/', addVehiculo, name='agrega_vehiculo'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/cliente/', clienteHome, name='clienteHome'),
    path('home/cliente/diagnostico/', diagnostico, name='diagnostico'),
    path('home/buscar/', search, name='search'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
