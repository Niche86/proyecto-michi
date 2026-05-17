# -*- coding: utf-8 -*-
from django.test import TestCase
from django.urls import reverse
from testmichi.models import Gato, Pregunta, Respuesta


class TestVistaTest(TestCase):
    def setUp(self):
        # Crear 5 gatos
        self.gato_kb = Gato.objects.create(nombre="Keyboard Cat", descripcion="Chambeador", imagen="kb.gif")
        self.gato_cc = Gato.objects.create(nombre="Crying Cat", descripcion="Estresado", imagen="cc.gif")
        self.gato_tif = Gato.objects.create(nombre="This is Fine Cat", descripcion="Optimista", imagen="tif.gif")
        self.gato_lc = Gato.objects.create(nombre="Loading Cat", descripcion="Confundido", imagen="lc.gif")
        self.gato_lz = Gato.objects.create(nombre="Lazy Cat", descripcion="Procrastinador", imagen="lz.gif")

        # Crear 1 pregunta con 3 respuestas (todas apuntan a Keyboard Cat para asegurar el resultado)
        self.pregunta = Pregunta.objects.create(texto="¿Pregunta de prueba?", orden=1)
        self.respuesta1 = Respuesta.objects.create(pregunta=self.pregunta, texto="Opción A", gato=self.gato_kb)
        Respuesta.objects.create(pregunta=self.pregunta, texto="Opción B", gato=self.gato_cc)
        Respuesta.objects.create(pregunta=self.pregunta, texto="Opción C", gato=self.gato_tif)

    def test_procesar_redirige_al_gato_esperado(self):
        """Al enviar siempre la misma respuesta, debe redirigir al gato correspondiente."""
        url = reverse('procesar')
        data = {
            f'pregunta_{self.pregunta.id}': self.respuesta1.id,
        }
        response = self.client.post(url, data)
        self.assertRedirects(response, reverse('resultado', kwargs={'gato_id': self.gato_kb.id}))
