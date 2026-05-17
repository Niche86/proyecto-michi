# GUÍA DE ESTUDIO - Proyecto "Qué Michi Eres"

Esta guía te permite explicar cada archivo y cada línea de código del proyecto. Léela antes del video y practica explicando en voz alta.

---

## 1. ESTRUCTURA GENERAL DEL PROYECTO

```
Proyecto Michi/
├── manage.py                  → Comando principal de Django
├── michiproject/              → Carpeta de configuración del proyecto
│   ├── __init__.py
│   ├── settings.py            → Configuración (base de datos, apps, etc.)
│   ├── urls.py                → Rutas principales del sitio
│   └── wsgi.py                → Configuración para despliegue
├── testmichi/                 → NUESTRA APLICACIÓN
│   ├── __init__.py
│   ├── models.py              → Tablas de la base de datos
│   ├── views.py               → Lógica de las páginas (Vistas Genéricas)
│   ├── urls.py                → Rutas de nuestra app
│   ├── admin.py               → Configuración del panel admin
│   ├── tests.py               → Pruebas automáticas
│   ├── templates/             → HTML de las páginas
│   │   └── testmichi/
│   │       ├── index.html     → Página del test
│   │       └── resultado.html → Página del resultado
│   ├── static/                → Imágenes, CSS, JS
│   │   └── testmichi/gifs/    → GIFs de los gatos
│   └── management/
│       └── commands/
│           └── seed.py        → Comando para cargar datos
└── db.sqlite3                 → Base de datos
```

---

## 2. EXPLICACIÓN ARCHIVO POR ARCHIVO

---

### 2.1 manage.py

**¿Qué hace?** Es el punto de entrada. Django te da este archivo para correr comandos.

**Comandos que usamos:**
```bash
python manage.py runserver      # Corre el servidor local
python manage.py migrate        # Crea las tablas en SQLite
python manage.py seed           # Carga los gatos, preguntas y respuestas
python manage.py test           # Ejecuta las pruebas
python manage.py createsuperuser # Crea usuario admin
```

**En el video puedes decir:** *"Este archivo lo crea Django automáticamente. Nosotros solo lo usamos para correr comandos."*

---

### 2.2 michiproject/settings.py

**¿Qué hace?** Configura todo el proyecto: qué apps usa, qué base de datos, idioma, etc.

**Las líneas clave que modificamos:**

```python
INSTALLED_APPS = [
    'django.contrib.admin',       # Panel de administración
    'django.contrib.auth',        # Sistema de usuarios
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'testmichi',                  # ← NUESTRA APP. Aquí la registramos
]
```

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Usamos SQLite
        'NAME': BASE_DIR / 'db.sqlite3',         # Archivo de la BD
    }
}
```

```python
ALLOWED_HOSTS = ['*']  # Permitimos cualquier host (para Render)
```

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'testmichi' / 'templates'],  # Dónde busca HTML
        'APP_DIRS': True,
        ...
    }
]
```

**En el video:** *"En settings registramos nuestra app 'testmichi', configuramos SQLite como base de datos, y le dijimos a Django dónde buscar los templates HTML."*

---

### 2.3 michiproject/urls.py

**¿Qué hace?** Define las URLs principales del sitio.

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),           # /admin → Panel admin
    path('', include('testmichi.urls')),       # '' → Todo lo demás lo maneja testmichi
]
```

- `path('admin/', admin.site.urls)` → Cuando entras a `/admin`, Django carga el panel.
- `path('', include('testmichi.urls'))` → Cualquier otra URL la maneja `testmichi/urls.py`.

**En el video:** *"Este archivo es como el directorio de rutas. Si alguien entra a /admin, va al panel. Cualquier otra dirección se la pasa a nuestra app testmichi."*

---

### 2.4 testmichi/models.py

**¿Qué hace?** Define las tablas de la base de datos. Cada clase = una tabla.

```python
from django.db import models

class Gato(models.Model):
    nombre = models.CharField(max_length=100)      # Texto corto
    descripcion = models.TextField()                # Texto largo
    imagen = models.CharField(max_length=255)       # Ruta del GIF

    def __str__(self):
        return self.nombre                          # Cómo se muestra en el admin
```

**Explicación línea por línea:**
- `class Gato(models.Model):` → Creamos la tabla "Gato". Hereda de Model.
- `nombre = models.CharField(max_length=100)` → Columna "nombre", máximo 100 caracteres.
- `descripcion = models.TextField()` → Columna "descripcion", texto sin límite.
- `imagen = models.CharField(...)` → Columna "imagen", guarda la ruta del archivo GIF.
- `def __str__(self):` → Método especial. Define cómo se ve el objeto en el admin.

```python
class Pregunta(models.Model):
    texto = models.TextField()
    orden = models.IntegerField(default=0)          # Número entero

    class Meta:
        ordering = ['orden']                        # Ordenar por este campo
```

- `class Meta:` → Configuración extra del modelo.
- `ordering = ['orden']` → Las preguntas se ordenan de menor a mayor según "orden".

```python
class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='respuestas')
    texto = models.TextField()
    gato = models.ForeignKey(Gato, on_delete=models.CASCADE, related_name='respuestas')
```

**Explicación clave:**
- `ForeignKey(Pregunta, ...)` → Relación de MUCHOS a UNO. Muchas respuestas pertenecen a UNA pregunta.
- `on_delete=models.CASCADE` → Si borras la pregunta, se borran sus respuestas.
- `related_name='respuestas'` → Desde una Pregunta puedes acceder a sus respuestas con `pregunta.respuestas.all()`.

**En el video:** *"Tenemos tres tablas: Gato, Pregunta y Respuesta. Respuesta tiene dos llaves foráneas: una apunta a Pregunta y otra a Gato. Es una relación muchos a uno."*

---

### 2.5 testmichi/admin.py

**¿Qué hace?** Configura cómo se ven los modelos en el panel de administración.

```python
from django.contrib import admin
from .models import Gato, Pregunta, Respuesta

@admin.register(Gato)
class GatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'imagen')
    list_display_links = ('nombre',)          # Hacer clic en el nombre para editar
```

- `@admin.register(Gato)` → Decorador que registra el modelo en el admin.
- `list_display` → Qué columnas se muestran en la lista.
- `list_display_links` → Qué campo es clickeable para editar.

```python
@admin.register(Respuesta)
class RespuestaAdmin(admin.ModelAdmin):
    list_display = ('id', 'texto', 'pregunta', 'gato')
    list_display_links = ('texto',)
    list_filter = ('gato', 'pregunta')        # Filtros en la barra lateral
```

- `list_filter` → Aparecen filtros en el panel para buscar por gato o pregunta.

**En el video:** *"Registramos los modelos en el admin para poder crear, editar y borrar registros desde el navegador sin tocar código."*

---

### 2.6 testmichi/views.py

**¿Qué hace?** La lógica de las páginas. Aquí usamos VISTAS GENÉRICAS de Django.

```python
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, View
from django.urls import reverse
from .models import Pregunta, Respuesta, Gato
from collections import Counter
import random
```

**Imports:**
- `ListView` → Vista genérica para mostrar una LISTA de objetos.
- `DetailView` → Vista genérica para mostrar el DETALLE de UN objeto.
- `View` → Vista base para crear lógica personalizada (como procesar formularios).
- `Counter` → Cuenta cuántas veces aparece cada elemento en una lista.

```python
class IndexView(ListView):
    model = Pregunta
    template_name = 'testmichi/index.html'
    context_object_name = 'preguntas'
    ordering = ['orden']
```

**Explicación paso a paso:**
1. `class IndexView(ListView):` → Heredamos de ListView.
2. `model = Pregunta` → Esta vista trabaja con el modelo Pregunta.
3. `template_name = 'testmichi/index.html'` → Usa ese archivo HTML.
4. `context_object_name = 'preguntas'` → En el template, la lista se llama `preguntas`.
5. `ordering = ['orden']` → Ordena por el campo "orden".

**¿Qué hace Django automáticamente?** Busca TODAS las preguntas, las ordena, y las manda al template. Tú no escribes esa consulta.

**En el video:** *"IndexView es una Vista Genérica. Django ya sabe cómo listar objetos. Yo solo le digo: usa el modelo Pregunta, este template, y ordénalas. Django hace la consulta a SQLite automáticamente."*

---

```python
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
```

**Explicación paso a paso:**
1. `class ProcesarView(View):` → Heredamos de View para lógica personalizada.
2. `def post(self, request):` → Solo responde a peticiones POST (envío de formulario).
3. `respuesta_ids = []` → Lista vacía para guardar los IDs de las respuestas elegidas.
4. `for key, value in request.POST.items():` → Recorre todo lo que envió el formulario.
5. `if key.startswith('pregunta_'):` → Filtra solo los campos que empiezan con "pregunta_".
6. `respuesta_ids.append(int(value))` → Convierte el ID a número y lo guarda.
7. `if not respuesta_ids:` → Si no eligió nada, vuelve al inicio.
8. `Respuesta.objects.filter(id__in=respuesta_ids)` → Consulta a la BD: "trae las respuestas con estos IDs".
9. `gatos = [r.gato for r in respuestas]` → Lista de comprensión. Extrae el gato de cada respuesta.
10. `Counter(gatos)` → Cuenta cuántas veces aparece cada gato.
11. `max_votos = max(conteo.values())` → Encuentra la cantidad más alta de votos.
12. `ganadores = [gato for gato, votos in conteo.items() if votos == max_votos]` → Si hay empate, guarda todos los que tienen el máximo.
13. `random.choice(ganadores)` → Si hay empate, elige uno al azar.
14. `redirect('resultado', gato_id=ganador.id)` → Redirige a la página del gato ganador.

**En el video:** *"ProcesarView recibe el formulario, extrae las respuestas del usuario, consulta la base de datos para saber qué gato corresponde a cada respuesta, cuenta los votos con Counter, resuelve empates con random.choice, y redirige al resultado."*

---

```python
class ResultadoView(DetailView):
    model = Gato
    template_name = 'testmichi/resultado.html'
    context_object_name = 'gato'
    pk_url_kwarg = 'gato_id'
```

**Explicación:**
1. `DetailView` → Muestra UN solo objeto.
2. `model = Gato` → Busca en la tabla Gato.
3. `pk_url_kwarg = 'gato_id'` → La URL tiene un número (`resultado/11/`), y este es el ID del gato.

**En el video:** *"ResultadoView es otra Vista Genérica. Recibe el ID del gato en la URL, busca ese gato en la base de datos, y lo manda al template para mostrar su nombre, descripción e imagen."*

---

### 2.7 testmichi/urls.py

**¿Qué hace?** Rutas específicas de nuestra app.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('procesar/', views.ProcesarView.as_view(), name='procesar'),
    path('resultado/<int:gato_id>/', views.ResultadoView.as_view(), name='resultado'),
]
```

- `path('', views.IndexView.as_view(), name='index')` → La raíz (`/`) carga IndexView.
- `path('procesar/', ...)` → `/procesar/` carga ProcesarView.
- `path('resultado/<int:gato_id>/', ...)` → `/resultado/11/` carga ResultadoView con el ID 11.
- `name='index'` → Nombre para usar en `{% url 'index' %}` y `redirect('index')`.

**En el video:** *"Las URLs conectan las direcciones web con las vistas. Si alguien entra a /procesar/, va a ProcesarView. Si entra a /resultado/11/, va a ResultadoView con el gato número 11."*

---

### 2.8 testmichi/tests.py

**¿Qué hace?** Prueba que la lógica funciona sin tener que abrir el navegador.

```python
from django.test import TestCase
from django.urls import reverse
from testmichi.models import Gato, Pregunta, Respuesta

class TestVistaTest(TestCase):
    def setUp(self):
        # Se ejecuta antes de cada test
        self.gato_kb = Gato.objects.create(nombre="el chambas", ...)
        self.pregunta = Pregunta.objects.create(texto="Pregunta de prueba", orden=1)
        self.respuesta1 = Respuesta.objects.create(pregunta=self.pregunta, texto="Opcion A", gato=self.gato_kb)
```

- `setUp` → Django corre esto antes de cada test.
- `reverse('index')` → Obtiene la URL a partir del nombre.

```python
    def test_index_usa_vista_generica(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'testmichi/index.html')
```

- `self.client.get(...)` → Simula un navegador haciendo petición GET.
- `assertEqual(response.status_code, 200)` → Verifica que la página cargó bien (200 = OK).
- `assertTemplateUsed(...)` → Verifica que usó el template correcto.

```python
    def test_procesar_redirige_al_gato_esperado(self):
        url = reverse('procesar')
        data = {'pregunta_%s' % self.pregunta.id: self.respuesta1.id}
        response = self.client.post(url, data)
        self.assertRedirects(response, reverse('resultado', kwargs={'gato_id': self.gato_kb.id}))
```

- `self.client.post(url, data)` → Simula enviar el formulario.
- `assertRedirects(...)` → Verifica que redirige a la URL del gato ganador.

**En el video:** *"Los tests crean datos de prueba en una base de datos temporal, simulan un usuario haciendo el test, y verifican que todo funciona. Si cambio algo y rompo la lógica, los tests me avisan."*

---

### 2.9 testmichi/management/commands/seed.py

**¿Qué hace?** Comando personalizado para cargar los datos iniciales.

```python
from django.core.management.base import BaseCommand
from testmichi.models import Gato, Pregunta, Respuesta

class Command(BaseCommand):
    help = 'Carga datos iniciales del test'

    def handle(self, *args, **kwargs):
        # Código que se ejecuta al correr: python manage.py seed
```

- `BaseCommand` → Clase base para crear comandos personalizados.
- `handle()` → Método que Django ejecuta cuando corres `python manage.py seed`.
- `get_or_create(...)` → Si el objeto ya existe, no lo duplica.

**En el video:** *"Cree un comando personalizado llamado 'seed'. Al correr python manage.py seed, crea los 5 gatos, 10 preguntas y 30 respuestas automáticamente. Uso get_or_create para no duplicar si ya existen."*

---

### 2.10 Templates HTML

#### index.html

```html
<form method="post" action="{% url 'procesar' %}">
    {% csrf_token %}
```

- `method="post"` → Envía los datos por POST (no por URL).
- `action="{% url 'procesar' %}"` → Django genera la URL `/procesar/`.
- `{% csrf_token %}` → Token de seguridad. Django lo exige en todos los formularios.

```html
    {% for pregunta in preguntas %}
        <input type="radio" name="pregunta_{{ pregunta.id }}" value="{{ respuesta.id }}" required>
```

- `preguntas` → Variable que envió IndexView (context_object_name).
- `pregunta.respuestas.all` → Gracias a `related_name='respuestas'` en el modelo.
- `name="pregunta_{{ pregunta.id }}"` → Nombre único para cada pregunta.
- `value="{{ respuesta.id }}"` → ID de la respuesta elegida.
- `required` → El navegador exige elegir una opción.

#### resultado.html

```html
{% load static %}
<img src="{% static gato.imagen %}" alt="{{ gato.nombre }}">
```

- `{% load static %}` → Carga el sistema de archivos estáticos.
- `{% static gato.imagen %}` → Genera la URL completa del GIF.

---

## 3. FLUJO DE DATOS (Cómo viaja la información)

```
Usuario entra a /
    ↓
urls.py → IndexView (ListView)
    ↓
Consulta a SQLite: SELECT * FROM preguntas ORDER BY orden
    ↓
Renderiza index.html con la lista de preguntas
    ↓
Usuario marca respuestas y da "Enviar"
    ↓
POST a /procesar/ → ProcesarView
    ↓
Extrae IDs de respuestas del formulario
    ↓
Consulta: SELECT * FROM respuestas WHERE id IN (...)
    ↓
Cuenta qué gato salió más veces (Counter)
    ↓
Redirige a /resultado/11/
    ↓
urls.py → ResultadoView (DetailView)
    ↓
Consulta: SELECT * FROM gatos WHERE id = 11
    ↓
Renderiza resultado.html con el gato
```

---

## 4. CONCEPTOS CLAVE PARA EL VIDEO

### ¿Qué son las Vistas Genéricas?
Son clases que Django ya tiene hechas para casos comunes. Tú configuras qué modelo y template usar, y Django hace el resto.
- **ListView** → Lista de objetos (IndexView)
- **DetailView** → Un solo objeto (ResultadoView)
- **View** → Para lógica personalizada (ProcesarView)

### ¿Qué es el ORM de Django?
Es la capa que te permite hablar con la base de datos usando Python, sin escribir SQL.
- `Pregunta.objects.all()` → SELECT * FROM preguntas
- `Respuesta.objects.filter(id__in=[1,2,3])` → SELECT * FROM respuestas WHERE id IN (1,2,3)
- `Gato.objects.get(id=11)` → SELECT * FROM gatos WHERE id = 11

### ¿Qué es una ForeignKey?
Es una relación "muchos a uno". Muchas respuestas pertenecen a una pregunta. En la base de datos, Django guarda el ID de la pregunta en la tabla de respuestas.

### ¿Qué es el panel Admin?
Es una interfaz automática que Django genera para gestionar los modelos. Nosotros solo lo registramos y configuramos qué columnas mostrar.

---

## 5. POSIBLES PREGUNTAS DEL PROFESOR

**"¿Por qué usaste Vistas Genéricas en vez de funciones?"**
> "Porque Django ya tiene la lógica común resuelta. ListView ya sabe cómo consultar, ordenar y paginar objetos. Yo le configuro el modelo y el template, y me ahorro código repetitivo."

**"¿Cómo funciona la relación entre Respuesta y Gato?"**
> "Respuesta tiene un ForeignKey a Gato. Es una relación muchos a uno: muchas respuestas apuntan al mismo gato. Django guarda el ID del gato en la tabla respuestas."

**"¿Qué pasa si hay empate en el test?"**
> "Uso Counter para contar votos. Si dos gatos tienen el mismo máximo, random.choice elige uno al azar. Así siempre hay un ganador."

**"¿Cómo cargaste los datos iniciales?"**
> "Cree un comando personalizado 'seed' que usa get_or_create. Al correr python manage.py seed, crea los gatos, preguntas y respuestas sin duplicar si ya existen."

**"¿Por qué SQLite?"**
> "Porque es una base de datos ligera en archivo. No necesita servidor externo, es perfecta para proyectos pequeños y para desplegar rápido en Render."

---

## 6. COMANDOS IMPORTANTES

```bash
# Crear migraciones (cambios en modelos)
python manage.py makemigrations

# Aplicar migraciones (crear tablas)
python manage.py migrate

# Cargar datos
python manage.py seed

# Correr tests
python manage.py test

# Correr servidor
python manage.py runserver

# Crear superusuario
python manage.py createsuperuser
```

---

**Fin de la guía. Éxito en el video y la entrega.**
