# ¿Qué Michi Eres? 🐱

Test de personalidad gamificado para estudiantes técnicos en entornos de alta exigencia académica. Descubre qué gato meme representa tu forma de enfrentar el estrés universitario.

## Problemática

En entornos universitarios de alta exigencia académica, los estudiantes técnicos raramente disponen de herramientas ligeras para reflexionar sobre sus patrones de comportamiento ante el estrés. Esta app utiliza un test de personalidad gamificado para que, de forma anónima y rápida, un grupo pueda identificar tendencias colectivas (ej: alta procrastinación, estrés crónico, confusión constante) y tomar decisiones de ritmo de trabajo.

## Instalación

```bash
# Clonar el repositorio
git clone <repo-url>
cd proyecto-michi

# Instalar dependencias
pip install -r requirements.txt

# Aplicar migraciones
python manage.py migrate

# Cargar datos iniciales
python manage.py seed

# Crear superusuario (opcional)
python manage.py createsuperuser

# Correr servidor
python manage.py runserver
```

## Uso

1. Accede a `http://localhost:8000` para hacer el test.
2. Responde las 10 preguntas y descubre qué gato eres.
3. Accede a `http://localhost:8000/admin` para gestionar preguntas, respuestas y gatos.

## Tests

```bash
python manage.py test
```

## Tecnologías

- Django 5.2
- SQLite
- Python 3.10+

## Despliegue

La app está configurada para desplegarse en Render usando Gunicorn.

```bash
gunicorn michiproject.wsgi:application
```
