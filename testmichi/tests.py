# -*- coding: utf-8 -*-
from django.test import TestCase
from django.urls import reverse
from testmichi.models import Gato, Pregunta, Respuesta


class TestVistaTest(TestCase):
    def setUp(self):
        self.gato_kb = Gato.objects.create(nombre="el chambas", descripcion="Chambeador", imagen="kb.gif")
        self.gato_cc = Gato.objects.create(nombre="El Lloricas", descripcion="Estresado", imagen="cc.gif")
        self.gato_tif = Gato.objects.create(nombre="Ta bien", descripcion="Optimista", imagen="tif.gif")
        self.gato_lc = Gato.objects.create(nombre="error de capa 8", descripcion="Confundido", imagen="lc.gif")
        self.gato_lz = Gato.objects.create(nombre="A colombia la esta matando la pereza", descripcion="Procrastinador", imagen="lz.gif")

        self.pregunta = Pregunta.objects.create(texto="Pregunta de prueba", orden=1)
        self.respuesta1 = Respuesta.objects.create(pregunta=self.pregunta, texto="Opcion A", gato=self.gato_kb)
        Respuesta.objects.create(pregunta=self.pregunta, texto="Opcion B", gato=self.gato_cc)
        Respuesta.objects.create(pregunta=self.pregunta, texto="Opcion C", gato=self.gato_tif)

    def test_index_usa_vista_generica(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'testmichi/index.html')

    def test_procesar_redirige_al_gato_esperado(self):
        url = reverse('procesar')
        data = {
            'pregunta_%s' % self.pregunta.id: self.respuesta1.id,
        }
        response = self.client.post(url, data)
        self.assertRedirects(response, reverse('resultado', kwargs={'gato_id': self.gato_kb.id}))

    def test_resultado_muestra_gato(self):
        url = reverse('resultado', kwargs={'gato_id': self.gato_kb.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.gato_kb.nombre)
