from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, View
from django.urls import reverse
from .models import Pregunta, Respuesta, Gato
from collections import Counter
import random


class IndexView(ListView):
    model = Pregunta
    template_name = 'testmichi/index.html'
    context_object_name = 'preguntas'
    ordering = ['orden']


class ProcesarView(View):
    def post(self, request):
        respuesta_ids = []
        for key, value in request.POST.items():
            if key.startswith('pregunta_'):
                respuesta_ids.append(int(value))

        if not respuesta_ids:
            return redirect('index')

        respuestas = Respuesta.objects.filter(id__in=respuesta_ids)
        gatos = [r.gato for r in respuestas]
        conteo = Counter(gatos)
        max_votos = max(conteo.values())
        ganadores = [gato for gato, votos in conteo.items() if votos == max_votos]
        ganador = random.choice(ganadores)

        return redirect('resultado', gato_id=ganador.id)


class ResultadoView(DetailView):
    model = Gato
    template_name = 'testmichi/resultado.html'
    context_object_name = 'gato'
    pk_url_kwarg = 'gato_id'
