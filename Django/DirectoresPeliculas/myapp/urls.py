from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('directores', views.directoresList, name='directores-list'),
    path('peliculas', views.peliculasList, name='peliculas-list'),
    path('peliculas/<int:pk>', views.peliculasDetalles, name='peliculas-detalles'),
    path('peliculasdirector/<int:pk>', views.peliculasPorDirector, name='peliculas-por-director'),
]
