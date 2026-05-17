# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from testmichi.models import Gato, Pregunta, Respuesta


class Command(BaseCommand):
    help = 'Carga datos iniciales del test'

    def handle(self, *args, **kwargs):
        # Crear gatos
        gatos_data = [
            {"nombre": "Keyboard Cat", "descripcion": "El chambeador. Resuelve rápido sin drama.", "imagen": "testmichi/gifs/keyboard-cat.gif"},
            {"nombre": "Crying Cat", "descripcion": "El estresado. Todo le sale mal.", "imagen": "testmichi/gifs/crying-cat.gif"},
            {"nombre": "This is Fine Cat", "descripcion": "El optimista. Ignora el caos.", "imagen": "testmichi/gifs/this-is-fine-cat.gif"},
            {"nombre": "Loading Cat", "descripcion": "El confundido. Procesando... pantalla azul mental.", "imagen": "testmichi/gifs/loading-cat.gif"},
            {"nombre": "Lazy Cat", "descripcion": "El procrastinador. 'Eso se hace mañana'.", "imagen": "testmichi/gifs/lazy-cat.gif"},
        ]

        for g in gatos_data:
            Gato.objects.get_or_create(nombre=g["nombre"], defaults=g)

        gato_kb = Gato.objects.get(nombre="Keyboard Cat")
        gato_cc = Gato.objects.get(nombre="Crying Cat")
        gato_tif = Gato.objects.get(nombre="This is Fine Cat")
        gato_lc = Gato.objects.get(nombre="Loading Cat")
        gato_lz = Gato.objects.get(nombre="Lazy Cat")

        preguntas_data = [
            {
                "texto": "Es medianoche y tu código explotó. ¿Qué haces?",
                "orden": 1,
                "respuestas": [
                    ("Arreglo rápido y sigo sin drama.", gato_kb),
                    ("Cierro la laptop y me voy a llorar a la cama.", gato_cc),
                    ('"Esto está bien, lo reviso mañana con café".', gato_tif),
                ]
            },
            {
                "texto": "Tienes parcial mañana y no estudiaste. ¿Tu plan?",
                "orden": 2,
                "respuestas": [
                    ("Miro el temario con cara de spinner, no sé por dónde empezar.", gato_lc),
                    ("No estudié, juego una partida y confío en el azar.", gato_lz),
                    ("Hago un café y tiro respuestas de memoria.", gato_kb),
                ]
            },
            {
                "texto": "El TransMilenio viene lleno en hora pico. ¿Tú?",
                "orden": 3,
                "respuestas": [
                    ("Espero el siguiente con música, no hay prisa.", gato_tif),
                    ("Me devuelvo a casa, no vale la pena el esfuerzo.", gato_lz),
                    ("Me meto como sea, tengo que llegar.", gato_kb),
                ]
            },
            {
                "texto": "Te toca trabajo en equipo para un proyecto. ¿Cómo actúas?",
                "orden": 4,
                "respuestas": [
                    ("Me estreso porque nadie hace las cosas como yo quiero.", gato_cc),
                    ("Hago la parte difícil yo solo, es más rápido.", gato_kb),
                    ("Miro el repositorio, miro el Discord, miro la pantalla... y no entiendo qué toca hacer.", gato_lc),
                ]
            },
            {
                "texto": "No entiendes un concepto del curso. ¿Qué haces?",
                "orden": 5,
                "respuestas": [
                    ("Busco en Stack Overflow y YouTube hasta entenderlo.", gato_kb),
                    ("Le pregunto al profe sin pena, todos aprendemos.", gato_tif),
                    ("Leo la explicación 5 veces y sigo sin captar. Mi mente está en buffer.", gato_lc),
                ]
            },
            {
                "texto": "Deadline en 2 horas y estás en blanco. ¿Reacción?",
                "orden": 6,
                "respuestas": [
                    ("Priorizo lo esencial y trabajo enfocado.", gato_kb),
                    ("Me congelo, abro redes sociales para evadirme.", gato_cc),
                    ('"Es imposible terminar", me recuesto y veo memes.', gato_lz),
                ]
            },
            {
                "texto": "Tu compañero entregó código spaghetti. ¿Tú?",
                "orden": 7,
                "respuestas": [
                    ("Lo acepto, si funciona no le muevo.", gato_tif),
                    ("Lo reescribo todo porque no soporto el desorden.", gato_kb),
                    ("Abro el archivo, miro 300 líneas en una función... y cierro el IDE.", gato_lc),
                ]
            },
            {
                "texto": "Reunión de proyecto domingo 8am. ¿Llegas?",
                "orden": 8,
                "respuestas": [
                    ("Voy tarde, estresado y con cara de pocos amigos.", gato_cc),
                    ("Llego puntual con lo que me tocaba hecho.", gato_kb),
                    ("Voy relajado, es solo una reunión, no pasa nada.", gato_tif),
                ]
            },
            {
                "texto": "Fin de semana libre después de una semana pesada. ¿Plan?",
                "orden": 9,
                "respuestas": [
                    ("Duermo, veo series y no respondo mensajes.", gato_lz),
                    ("Salgo con amigos y olvido que existe la universidad.", gato_tif),
                    ("Aprovecho para adelantar el proyecto del próximo mes.", gato_kb),
                ]
            },
            {
                "texto": "Hora de hacer deploy a producción. ¿Cómo procedes?",
                "orden": 10,
                "respuestas": [
                    ("Le digo a otro que lo haga, me da pánico romper algo.", gato_lz),
                    ("Estoy en constante refresh de la página con miedo.", gato_cc),
                    ("Miro la terminal, miro la documentación, miro la terminal otra vez... y no sé si darle enter.", gato_lc),
                ]
            },
        ]

        for p_data in preguntas_data:
            pregunta, _ = Pregunta.objects.get_or_create(
                orden=p_data["orden"],
                defaults={"texto": p_data["texto"]}
            )
            for r_texto, r_gato in p_data["respuestas"]:
                Respuesta.objects.get_or_create(
                    pregunta=pregunta,
                    texto=r_texto,
                    defaults={"gato": r_gato}
                )

        self.stdout.write(self.style.SUCCESS('Datos iniciales cargados correctamente.'))
