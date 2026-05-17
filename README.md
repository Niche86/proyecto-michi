# Que Michi Eres

Aplicacion web con Django para identificar patrones de comportamiento ante el estres universitario mediante un test de personalidad.

## Problematica

Los estudiantes tecnicos en entornos de alta exigencia academica no cuentan con herramientas simples para reflexionar sobre como manejan el estres. Esta aplicacion permite, de forma anonima y rapida, identificar tendencias como procrastinacion, estres cronico o confusion.

## Requisitos cumplidos

- Creacion de Vistas (Vistas Genericas: ListView, DetailView, View)
- Creacion de Modelos (Gato, Pregunta, Respuesta)
- Manejo de UrlConf
- Integracion de Formularios
- CRUD dentro de SQLite
- Integracion del panel Admin
- Testing

## Instalacion local

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py seed
python manage.py runserver
```

Abrir http://localhost:8000 en el navegador.

El panel admin esta en http://localhost:8000/admin
- Usuario: admin
- Contrasena: admin123

## Tests

```bash
python manage.py test
```

## Despliegue

La aplicacion esta lista para desplegarse en Render usando Gunicorn:

```bash
gunicorn michiproject.wsgi:application
```
