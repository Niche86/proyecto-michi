from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Prefetch
from .models import Pregunta, Respuesta, Gato
from collections import Counter
import random


def index(request):
    preguntas = Pregunta.objects.prefetch_related('respuestas').all()
    return render(request, 'testmichi/index.html', {'preguntas': preguntas})


def procesar(request):
    if request.method != 'POST':
        return redirect('index')

    respuesta_ids = []
    for key, value in request.POST.items():
        if key.startswith('pregunta_'):
            respuesta_ids.append(int(value))

    if not respuesta_ids:
        return redirect('index')

    respuestas = Respuesta.objects.filter(id__in=respuesta_ids).select_related('gato')
    conteo = Counter(r.gato for r in respuestas)
    max_votos = max(conteo.values())
    ganadores = [gato for gato, votos in conteo.items() if votos == max_votos]
    ganador = random.choice(ganadores)

    return redirect('resultado', gato_id=ganador.id)


def resultado(request, gato_id):
    gato = get_object_or_404(Gato, id=gato_id)
    return render(request, 'testmichi/resultado.html', {'gato': gato})
