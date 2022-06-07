from django.db import models


class Director(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Pelicula(models.Model):
    director = models.ForeignKey(Director, related_name='pelicula', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo
