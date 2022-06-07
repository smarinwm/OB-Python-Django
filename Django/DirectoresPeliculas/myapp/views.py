from django.shortcuts import render

from myapp.models import Director, Pelicula


def index(request):
    context = {
        'titulo': "Directores y Películas.",
        'seccion': "Opciones."
    }
    return render(request, 'primera.html', context)


def directoresList(request):
    context = {
        'titulo': "Listado completo de los directores.",
        'seccion': "Pulsa para ver las películas del director.",
        'directores_list': Director.objects.all()
    }
    return render(request, 'directores.html', context)


def peliculasList(request):
    context = {
        'titulo': "Listado completo de las películas.",
        'seccion': "Pulsa para ver el detalle de la película.",
        'peliculas_list': Pelicula.objects.all()
    }
    return render(request, 'peliculas-list.html', context)


def peliculasPorDirector(request, pk):
    context = {
        'titulo': "Películas por director.",
        'seccion': "Pulsa para ver el detalle de la película.",
        'peliculas_por_director': Pelicula.objects.filter(director_id=pk)
    }
    return render(request, 'peliculas-por-director.html', context)


def peliculasDetalles(request, pk):
    context = {
        'titulo': "Descripción de la película.",
        'peliculas_detalles': Pelicula.objects.get(id=pk)
    }
    return render(request, 'peliculas-detalles.html', context)
