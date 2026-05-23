# MANUAL DE DEFENSA - Proyecto "Que Michi Eres"

Documento para responder cualquier pregunta del profesor en la sustentacion.

---

## 1. PREGUNTA CLAVE: POR QUE ESTE PROYECTO?

### La problematica real
Los grupos de trabajo universitario se desarman no por falta de conocimiento, sino por **friccion por estres no gestionado**.

Cada estudiante reacciona diferente ante la presion:
- El chambeador se carga todo y se resiente
- El procrastinador deja todo para ultima hora
- El ansioso se paraliza
- El optimista ignora los problemas
- El confundido no sabe por donde empezar

**Y nadie habla de eso.** Los grupos asumen que todos trabajan igual.

### Por que no un CRUD generico?
Porque la IA sugiere eso de primeras. Un test de personalidad con gatos memes para identificar patrones de estres en grupos universitarios es un nicho especifico que no sale en los prompts genericos.

---

## 2. ARQUITECTURA GENERAL

```
Usuario -> Navegador -> Render (servidor)
                          |
                          v
                    Gunicorn (servidor WSGI)
                          |
                          v
                    Django (aplicacion)
                          |
            +-------------+-------------+
            |             |             |
            v             v             v
        URLs          Vistas        Modelos
            |             |             |
            v             v             v
    testmichi/urls   views.py     SQLite (db)
            |             |             |
            v             v             v
        Templates    Logica de     Tablas:
                      negocio      Gato
                                   Pregunta
                                   Respuesta
```

---

## 3. DECISIONES TECNICAS Y SUS JUSTIFICACIONES

### Por que Django y no Flask?
Django incluye todo lo necesario: ORM, panel admin, sistema de autenticacion, manejo de templates. Flask requiere instalar y configurar todo eso manualmente. Para un proyecto academico con fecha limite, Django es mas rapido.

### Por que SQLite y no PostgreSQL?
Porque es una tarea universitaria con un solo usuario concurrente (el profesor evaluando). SQLite es un archivo, no requiere servidor externo, y es perfectamente suficiente para este nivel de trafico. PostgreSQL seria como usar un camion de carga para llevar una mochila.

### Por que vistas genericas y no funciones?
Porque Django ya resolvio los casos comunes. ListView sabe como listar objetos, DetailView sabe como mostrar uno solo. Yo solo configuro modelo y template. Esto reduce codigo repetitivo y errores. Es una practica recomendada por la documentacion oficial de Django.

### Por que WhiteNoise?
En produccion (DEBUG=False), Django no sirve archivos estaticos (imagenes, CSS). WhiteNoise es un middleware que se pone entre Gunicorn y Django para servir esos archivos desde la carpeta staticfiles. Sin el, los GIFs no se ven en Render.

### Por que Gunicorn?
El servidor de desarrollo de Django (`runserver`) no es seguro para produccion. Gunicorn es un servidor WSGI de produccion que maneja multiples peticiones concurrentes. Render lo requiere.

### Por que ALLOWED_HOSTS = ['*']?
Porque Render asigna un dominio dinamico. No se cual es hasta que se despliega. Con ['*'] acepto cualquier dominio. En un proyecto real usaria el dominio exacto.

### Por que el formulario usa POST y no GET?
Porque GET envia los datos por la URL (visibles, limitados en tamano, quedan en el historial). POST envia los datos en el cuerpo de la peticion, es mas seguro y no tiene limite de tamano. Ademas Django requiere POST para acciones que modifican datos.

### Por que CSRF token?
Es una proteccion contra ataques de Cross-Site Request Forgery. Django lo exige en todos los formularios POST. Si alguien crea un formulario falso en otro sitio apuntando a mi app, el token no coincide y la peticion se rechaza.

---

## 4. EXPLICACION DETALLADA DEL FLUJO

### 4.1 Cuando el usuario entra a la pagina

1. El navegador hace una peticion GET a `/`
2. La URL `urls.py` del proyecto la redirige a `testmichi/urls.py`
3. `testmichi/urls.py` la mapea a `IndexView`
4. `IndexView` (ListView) hace automaticamente: `SELECT * FROM preguntas ORDER BY orden`
5. Django envia los resultados al template `index.html`
6. El template renderiza las 10 preguntas con sus respuestas usando el tag `{% for %}`
7. El navegador muestra el formulario

### 4.2 Cuando el usuario envia el formulario

1. El navegador hace una peticion POST a `/procesar/`
2. Django verifica el token CSRF
3. `ProcesarView.post()` recibe `request.POST`, que es un diccionario con los datos del formulario
4. El metodo recorre cada campo que empieza con `pregunta_` y extrae el ID de la respuesta elegida
5. Hace la consulta: `SELECT * FROM respuestas WHERE id IN (ids)`
6. De cada respuesta, extrae el objeto `gato` relacionado (gracias a la ForeignKey)
7. Usa `Counter` para contar cuantas veces aparece cada gato
8. Encuentra el maximo de votos
9. Si hay empate, usa `random.choice` para elegir uno
10. Redirige a `/resultado/ID_DEL_GATO/`

### 4.3 Cuando se muestra el resultado

1. El navegador hace GET a `/resultado/11/`
2. La URL captura el numero `11` como `gato_id`
3. `ResultadoView` (DetailView) hace: `SELECT * FROM gatos WHERE id = 11`
4. El template `resultado.html` recibe el objeto `gato`
5. Muestra `gato.nombre`, `gato.descripcion`, y la imagen usando `{% static %}`

---

## 5. EL PANEL ADMIN COMO CRUD

CRUD significa Create, Read, Update, Delete. El panel admin de Django hace todo eso automaticamente.

- **Create:** Click en "Add" -> llenas el formulario -> Save
- **Read:** La lista muestra todos los registros
- **Update:** Click en un registro -> editas -> Save
- **Delete:** Seleccionas registros -> Action "Delete" -> Go

Todo esto sin escribir una sola linea de codigo extra. Django genera la interfaz a partir de los modelos.

---

## 6. LOS TESTS: QUE PRUEBAN Y POR QUE

| Test | Que verifica | Por que importa |
|------|--------------|----------------|
| test_index_usa_vista_generica | Que la pagina principal cargue (status 200) y use el template correcto | Si rompo la URL o cambio el nombre del template, este test falla |
| test_procesar_redirige_al_gato_esperado | Que al enviar siempre la misma respuesta, redirija al gato correcto | Verifica la logica de conteo y la redireccion |
| test_resultado_muestra_gato | Que la pagina de resultado contenga el nombre del gato | Verifica que DetailView busque el gato correcto |

Los tests usan una base de datos temporal que se crea y destruye automaticamente. No tocan tu base de datos real.

---

## 7. RESPUESTAS A PREGUNTAS DIFICILES DEL PROFE

### "Por que no usaste API REST?"
> Porque el proyecto no lo requiere. Es una aplicacion web tradicional con server-side rendering. Las vistas genericas generan HTML directamente. Una API REST seria necesaria si tuviera un frontend separado (React, Vue), pero aqui Django maneja todo.

### "Por que no usaste PostgreSQL/MySQL?"
> Para el nivel de trafico de este proyecto (un solo evaluador), SQLite es suficiente. Es un archivo autocontenido, no requiere configurar un servidor de base de datos separado, y simplifica el despliegue. En un proyecto real con miles de usuarios concurrentes, migraria a PostgreSQL.

### "Por que los nombres de los gatos estan en espanol coloquial?"
> Porque la app esta dirigida a estudiantes colombianos. Usar humor local ("el chambas", "error de capa 8", "A colombia la esta matando la pereza") hace que la app sea mas cercana y aumenta la probabilidad de que los estudiantes realmente la usen. Un test con nombres genericos en ingles no conectaria con el publico objetivo.

### "Como garantizas que cada gato tenga la misma probabilidad de salir?"
> Cada gato aparece exactamente 6 veces entre las 30 respuestas totales (3 respuestas por pregunta x 10 preguntas). Como cada pregunta tiene solo una respuesta por gato, matematicamente todos tienen la misma probabilidad si el usuario responde al azar. En la practica, las respuestas del usuario sesgan el resultado, que es precisamente el objetivo: identificar su patron de comportamiento.

### "Que pasa si hay empate?"
> Uso `random.choice` sobre la lista de ganadores. Si dos gatos tienen el mismo numero maximo de votos, elige uno al azar. Esto evita que la app se rompa o quede sin resultado.

### "Por que no guardaste los resultados de cada test en la base de datos?"
> Porque el anonimato es parte del diseno. La app no requiere login ni guarda resultados personales. Es una herramienta de hielo roto para grupos, no un sistema de seguimiento individual. Si en el futuro se necesita analytics, se puede agregar un modelo `Resultado` con fecha y gato ganador.

### "Como funciona el ORM de Django?"
> El ORM (Object-Relational Mapping) es la capa que traduce codigo Python a consultas SQL. Por ejemplo:
> - `Pregunta.objects.all()` se convierte en `SELECT * FROM testmichi_pregunta`
> - `Respuesta.objects.filter(id__in=[1,2,3])` se convierte en `SELECT * FROM testmichi_respuesta WHERE id IN (1, 2, 3)`
> - `gato.respuestas.all()` usa la relacion inversa definida por `related_name='respuestas'` en la ForeignKey
> Esto me permite trabajar con objetos Python en lugar de escribir SQL manualmente.

### "Por que DEBUG = False en produccion?"
> Porque en modo DEBUG Django muestra informacion sensible cuando ocurre un error (traza completa, configuracion, variables). Eso es un riesgo de seguridad. En produccion se desactiva y Django muestra una pagina de error generica.

### "Como se despliega la app?"
> El codigo esta en GitHub. Render se conecta al repositorio y, en cada push a la rama main, reconstruye y redepliega automaticamente. El proceso es:
> 1. Render clona el repo
> 2. Ejecuta `build.sh` (instala dependencias, migra base de datos, recolecta estaticos)
> 3. Inicia Gunicorn con `gunicorn michiproject.wsgi:application`
> 4. La app queda disponible en la URL publica

---

## 8. MAPA MENTAL DEL PROYECTO

Si te pierdes, recuerda esta estructura:

```
USUARIO
   |
   v
Navegador --HTTP--> Render --Gunicorn--> Django
                                           |
                    +----------------------+----------------------+
                    |                      |                      |
                    v                      v                      v
                 Models                 Views                 Templates
                    |                      |                      |
            +-------+-------+      +-------+-------+      +-------+-------+
            |       |       |      |       |       |      |       |       |
            v       v       v      v       v       v      v       v       v
          Gato  Pregunta Respuesta List  Detail  View   index  resultado  admin
```

---

## 9. COMANDOS CLAVE QUE DEBES SABER DE MEMORIA

| Comando | Para que sirve |
|---------|----------------|
| `python manage.py runserver` | Corre el servidor local |
| `python manage.py migrate` | Aplica migrations (crea/actualiza tablas) |
| `python manage.py makemigrations` | Crea un archivo migration cuando cambias models.py |
| `python manage.py test` | Ejecuta los tests |
| `python manage.py createsuperuser` | Crea usuario para el panel admin |
| `python manage.py collectstatic` | Junta todos los archivos estaticos en una carpeta |
| `git push origin main` | Sube cambios a GitHub |

---

## 10. ERRORES COMUNES Y SOLUCIONES

| Error | Causa | Solucion |
|-------|-------|----------|
| 403 CSRF | Token expiro o sesion cambio | Recargar la pagina del formulario |
| 404 en GIFs | WhiteNoise no configurado | Verificar STATIC_ROOT y whitenoise en MIDDLEWARE |
| ModuleNotFoundError | Falta instalar una libreria | `pip install nombre-del-paquete` |
| NoReverseMatch | URL mal escrita en redirect | Verificar que el nombre y los parametros coincidan con urls.py |
| Tests fallan | Cambiaste algo y rompiste logica | Revisar el ultimo cambio hecho |

---

## 11. MENSAJE FINAL PARA LA SUSTENTACION

Si el profe te pregunta algo que no sabes, usa esta formula:

> "En este proyecto decidi [X] porque [razon practica]. Si el proyecto escalara a [Y], la siguiente mejora seria [Z]."

Ejemplo:
> "Decidi SQLite porque es una tarea academica con trafico minimo. Si esto creciera a cientos de usuarios diarios, la siguiente mejora seria migrar a PostgreSQL y agregar un modelo Resultado para guardar estadisticas anonimas."

Esto demuestra que entiendes las limitaciones actuales y sabes hacia donde evolucionaria el proyecto.

---

**SUERTE EN LA SUSTENTACION.**
