from django.contrib import admin

from myapp.models import Director, Pelicula


class DirectorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido')


class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion')


admin.site.register(Director, DirectorAdmin)
admin.site.register(Pelicula, PeliculaAdmin)
