# -*- coding: utf-8 -*-
from django.db import migrations


def seed_data(apps, schema_editor):
    Gato = apps.get_model('testmichi', 'Gato')
    Pregunta = apps.get_model('testmichi', 'Pregunta')
    Respuesta = apps.get_model('testmichi', 'Respuesta')

    gatos_data = [
        {"nombre": "el chambas", "descripcion": "El chambeador. Resuelve rapido sin drama.", "imagen": "testmichi/gifs/keyboard-cat.gif"},
        {"nombre": "El Lloricas", "descripcion": "El estresado. Todo le sale mal.", "imagen": "testmichi/gifs/crying-cat.gif"},
        {"nombre": "Ta bien", "descripcion": "El optimista. Ignora el caos.", "imagen": "testmichi/gifs/this-is-fine-cat.gif"},
        {"nombre": "error de capa 8", "descripcion": "El confundido. Procesando... pantalla azul mental.", "imagen": "testmichi/gifs/loading-cat.gif"},
        {"nombre": "A colombia la esta matando la pereza", "descripcion": "El procrastinador. 'Eso se hace manana'.", "imagen": "testmichi/gifs/lazy-cat.gif"},
    ]

    gato_objs = {}
    for g in gatos_data:
        obj, _ = Gato.objects.get_or_create(nombre=g["nombre"], defaults=g)
        gato_objs[g["nombre"]] = obj

    preguntas_data = [
        {
            "texto": "Es medianoche y tu codigo exploto. Que haces?",
            "orden": 1,
            "respuestas": [
                ("Arreglo rapido y sigo sin drama.", "el chambas"),
                ("Cierro la laptop y me voy a llorar a la cama.", "El Lloricas"),
                ('"Esto esta bien, lo reviso manana con cafe".', "Ta bien"),
            ]
        },
        {
            "texto": "Tienes parcial manana y no estudiaste. Tu plan?",
            "orden": 2,
            "respuestas": [
                ("Miro el temario con cara de spinner, no se por donde empezar.", "error de capa 8"),
                ("No estudie, juego una partida y confio en el azar.", "A colombia la esta matando la pereza"),
                ("Hago un cafe y tiro respuestas de memoria.", "el chambas"),
            ]
        },
        {
            "texto": "El TransMilenio viene lleno en hora pico. Tu?",
            "orden": 3,
            "respuestas": [
                ("Espero el siguiente con musica, no hay prisa.", "Ta bien"),
                ("Me devuelvo a casa, no vale la pena el esfuerzo.", "A colombia la esta matando la pereza"),
                ("Me meto como sea, tengo que llegar.", "el chambas"),
            ]
        },
        {
            "texto": "Te toca trabajo en equipo para un proyecto. Como actuas?",
            "orden": 4,
            "respuestas": [
                ("Me estreso porque nadie hace las cosas como yo quiero.", "El Lloricas"),
                ("Hago la parte dificil yo solo, es mas rapido.", "el chambas"),
                ("Miro el repositorio, miro el Discord, miro la pantalla... y no entiendo que toca hacer.", "error de capa 8"),
            ]
        },
        {
            "texto": "No entiendes un concepto del curso. Que haces?",
            "orden": 5,
            "respuestas": [
                ("Busco en Stack Overflow y YouTube hasta entenderlo.", "el chambas"),
                ("Le pregunto al profe sin pena, todos aprendemos.", "Ta bien"),
                ("Leo la explicacion 5 veces y sigo sin captar. Mi mente esta en buffer.", "error de capa 8"),
            ]
        },
        {
            "texto": "Deadline en 2 horas y estas en blanco. Reaccion?",
            "orden": 6,
            "respuestas": [
                ("Priorizo lo esencial y trabajo enfocado.", "el chambas"),
                ("Me congelo, abro redes sociales para evadirme.", "El Lloricas"),
                ('"Es imposible terminar", me recuesto y veo memes.', "A colombia la esta matando la pereza"),
            ]
        },
        {
            "texto": "Tu companero entrego codigo spaghetti. Tu?",
            "orden": 7,
            "respuestas": [
                ("Lo acepto, si funciona no le muevo.", "Ta bien"),
                ("Lo reescribo todo porque no soporto el desorden.", "el chambas"),
                ("Abro el archivo, miro 300 lineas en una funcion... y cierro el IDE.", "error de capa 8"),
            ]
        },
        {
            "texto": "Reunion de proyecto domingo 8am. Llegas?",
            "orden": 8,
            "respuestas": [
                ("Voy tarde, estresado y con cara de pocos amigos.", "El Lloricas"),
                ("Llego puntual con lo que me tocaba hecho.", "el chambas"),
                ("Voy relajado, es solo una reunion, no pasa nada.", "Ta bien"),
            ]
        },
        {
            "texto": "Fin de semana libre despues de una semana pesada. Plan?",
            "orden": 9,
            "respuestas": [
                ("Duermo, veo series y no respondo mensajes.", "A colombia la esta matando la pereza"),
                ("Salgo con amigos y olvido que existe la universidad.", "Ta bien"),
                ("Aprovecho para adelantar el proyecto del proximo mes.", "el chambas"),
            ]
        },
        {
            "texto": "Hora de hacer deploy a produccion. Como procedes?",
            "orden": 10,
            "respuestas": [
                ("Le digo a otro que lo haga, me da panico romper algo.", "A colombia la esta matando la pereza"),
                ("Estoy en constante refresh de la pagina con miedo.", "El Lloricas"),
                ("Miro la terminal, miro la documentacion, miro la terminal otra vez... y no se si darle enter.", "error de capa 8"),
            ]
        },
    ]

    for p_data in preguntas_data:
        pregunta, _ = Pregunta.objects.get_or_create(
            orden=p_data["orden"],
            defaults={"texto": p_data["texto"]}
        )
        for r_texto, r_gato_nombre in p_data["respuestas"]:
            Respuesta.objects.get_or_create(
                pregunta=pregunta,
                texto=r_texto,
                defaults={"gato": gato_objs[r_gato_nombre]}
            )


def reverse_seed(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('testmichi', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_data, reverse_seed),
    ]
