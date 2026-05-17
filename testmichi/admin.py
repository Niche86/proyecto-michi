from django.contrib import admin
from .models import Gato, Pregunta, Respuesta


@admin.register(Gato)
class GatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'imagen')
    list_display_links = ('nombre',)


@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('id', 'texto', 'orden')
    list_display_links = ('texto',)


@admin.register(Respuesta)
class RespuestaAdmin(admin.ModelAdmin):
    list_display = ('id', 'texto', 'pregunta', 'gato')
    list_display_links = ('texto',)
    list_filter = ('gato', 'pregunta')
