
from django.urls import path
# se importa las vistas de la aplicaci�n
from financiero import views


urlpatterns = [
        path('', views.bancos, name='bancos'),
 ]
