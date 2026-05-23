# GUION PARA EL VIDEO (Maximo 10 minutos) - VERSION DETALLADA

## PREPARACION ANTES DE GRABAR (Haz esto 10 min antes)

### Paso 1: Abre las aplicaciones necesarias

Abre exactamente estas 3 ventanas:

1. **VS Code** - Con el proyecto abierto
2. **Terminal** - PowerShell o CMD, en la carpeta del proyecto
3. **Navegador Chrome/Edge** - Con 3 pestanas listas (ver mas abajo)

Cierra todo lo demas: WhatsApp, Spotify, Discord, notificaciones del celular.

### Paso 2: Corre los comandos en la terminal (en este orden)

Abre la terminal en la carpeta del proyecto (`C:\Users\klean\OneDrive\Desktop\Proyecto Michi`) y ejecuta:

```bash
# Comando 1: Activa el servidor de Django
python manage.py runserver
```

Dejalo corriendo. No cierres la terminal.

Abre una **segunda terminal** (Ctrl+Shift+Ñ en VS Code, o nueva pestana) y ejecuta:

```bash
# Comando 2: Carga los datos
python manage.py seed
```

Deberia decir: "Datos iniciales cargados correctamente."

Si dice que ya existen, no hay problema.

### Paso 3: Abre las URLs en el navegador

Abre exactamente estas 3 pestanas:

| Pestana | URL exacta | Que tiene que mostrar |
|---------|-----------|----------------------|
| 1 | `http://localhost:8000/` | El test con las 10 preguntas |
| 2 | `http://localhost:8000/admin` | Login del panel admin |
| 3 | `https://github.com/TU_USUARIO/proyecto-michi` | Tu repositorio (cuando lo subas) |

En la pestana del admin (`/admin`), inicia sesion con:
- Usuario: `admin`
- Contraseña: `admin123`

Dejalo ya logueado para no perder tiempo en el video.

### Paso 4: Configura VS Code

En VS Code, abre estos archivos en pestanas (para no buscarlos durante el video):

1. `testmichi/models.py`
2. `testmichi/views.py`
3. `testmichi/urls.py`
4. `testmichi/tests.py`

Pon el zoom al 150%: `Ctrl + +` (apretalo 3 veces)

### Paso 5: Configura la terminal para el video

En una tercera terminal (sin cerrar la del servidor), ten listo este comando pero NO lo corras todavia:

```bash
python manage.py test
```

Lo vas a correr EN VIVO durante el video.

---

## ESTRUCTURA DE PANTALLA PARA EL VIDEO

No uses diapositivas. Usa esta estructura:

```
+------------------+
|  NAVEGADOR       |  → Para mostrar la app funcionando
|  (localhost:8000)|
+------------------+
        ↓  (cambias ventana con Alt+Tab)
+------------------+
|  VS CODE         |  → Para mostrar el codigo
|  (zoom 150%)     |
+------------------+
        ↓  (cambias ventana con Alt+Tab)
+------------------+
|  TERMINAL        |  → Para correr tests
+------------------+
```

---

## GUION PASO A PASO

### 0:00 - 0:45 → INTRO + PROBLEMATICA

**Pantalla:** Tu cara (si sale tu cara) o la app en `localhost:8000`.

**Di exactamente esto (o con tus palabras):**

> "Hola, mi nombre es [tu nombre] y este es mi proyecto final llamado 'Que Michi Eres'.
>
> La problematica que identifique es esta: en los grupos de trabajo universitario, especialmente en carreras tecnicas, cada persona maneja el estres de forma diferente. Hay quienes procrastinan, otros se paralizan, otros actuan como si nada pasara. El problema es que nunca paramos a identificar eso, y los grupos se desarman por friccion, no por falta de conocimiento.
>
> Mi app es un test de personalidad gamificado usando gatos memes, para que un grupo de estudiantes se entienda mejor y organice su ritmo de trabajo."

**Consejo:** Practica esto 2 veces antes de grabar. No leas, habla natural.

---

### 0:45 - 2:00 → DEMO DE LA APP FUNCIONANDO

**Pantalla:** Navegador en `http://localhost:8000/`

**Acciones que debes hacer (en orden):**

1. Muestra la pagina completa con el scroll
2. Di: "Aqui estan las 10 preguntas sobre situaciones universitarias reales"
3. Haz clic en la PRIMERA respuesta de la pregunta 1
4. Haz clic en la PRIMERA respuesta de la pregunta 2
5. Baja con scroll hasta el boton verde
6. Di: "Voy a enviar el formulario..."
7. Haz clic en "Descubrir mi Michi"

**Di esto mientras haces clic:**

> "Voy a hacer el test. Voy a elegir algunas respuestas rapidamente... y al enviar, me dice que soy [el gato que salga]. Me muestra su imagen, su descripcion, y puedo volver a hacer el test."

**Consejo:** No hagas las 10 preguntas. Solo marca 2-3 y envia. El video no debe durar mas de 1 min aqui.

---

### 2:00 - 3:30 → MODELOS Y BASE DE DATOS

**Pantalla:** VS Code con el archivo `testmichi/models.py` abierto.

**Acciones:**
1. Alt+Tab para cambiar a VS Code
2. Asegurate de que `models.py` este abierto
3. Muestra las 3 clases con el cursor (no hagas scroll rapido, ve lento)

**Di esto (senalando con el mouse cada parte):**

> "Ahora les muestro los modelos, que son las tablas de la base de datos. Tengo tres modelos.
>
> Primero, Gato. Guarda el nombre, la descripcion y la ruta del GIF.
>
> Segundo, Pregunta. Guarda el texto y el orden en que se muestra.
>
> Tercero, Respuesta. Esta es la mas importante. Tiene dos llaves foraneas: una apunta a Pregunta y otra apunta a Gato. Esto es una relacion muchos a uno. Muchas respuestas pertenecen a una pregunta, y muchas respuestas pueden apuntar al mismo gato."

**Muestra especificamente:**
- `class Gato(models.Model):`
- `class Pregunta(models.Model):`
- Las dos lineas de `ForeignKey` en la clase Respuesta
- El `class Meta: ordering = ['orden']`

**Consejo:** No expliques cada palabra, solo los conceptos clave. Si te preguntan "que es ForeignKey", di: "Es una relacion de muchos a uno en la base de datos."

---

### 3:30 - 5:00 → VISTAS GENERICAS

**Pantalla:** VS Code con el archivo `testmichi/views.py` abierto.

**Acciones:**
1. Cambia a la pestana de `views.py` (Ctrl+Tab o clic en la pestana)
2. Muestra las 3 clases con el cursor

**Di esto:**

> "Para las vistas use Vistas Genericas de Django, que es una de las tematicas vistas en clase. Tengo tres vistas.
>
> IndexView hereda de ListView. Esto significa que Django ya sabe como listar objetos. Yo solo le configuro: usa el modelo Pregunta, este template, y ordénalas por el campo orden. Django hace la consulta a SQLite automaticamente.
>
> ResultadoView hereda de DetailView. Muestra un solo objeto, el gato ganador. Recibe el ID del gato por la URL.
>
> Y ProcesarView hereda de View. Aqui esta la logica personalizada. Recibe las respuestas del formulario, extrae los IDs, busca las respuestas en la base de datos, cuenta cuantas veces salio cada gato usando Counter, resuelve empates con random.choice, y redirige al resultado."

**Muestra especificamente:**
- `class IndexView(ListView):` y sus 4 lineas de configuracion
- `class ResultadoView(DetailView):` y sus lineas
- `class ProcesarView(View):` y la parte de `Counter` + `random.choice`

**Frase clave que el profe quiere escuchar:** *"Use Vistas Genericas porque Django ya tiene la logica comun resuelta. Yo solo configuro el modelo y el template, y me ahorro codigo repetitivo."*

---

### 5:00 - 5:45 → URLS Y FORMULARIOS

**Pantalla:** VS Code con `testmichi/urls.py` abierto, y luego `index.html`.

**Acciones:**
1. Muestra `testmichi/urls.py`
2. Luego cambia a `testmichi/templates/testmichi/index.html`

**Di esto:**

> "Las URLs estan en dos archivos. El principal incluye las rutas de nuestra app. Y dentro de testmichi tengo tres rutas: la raiz va a IndexView, procesar va a ProcesarView, y resultado recibe un numero que es el ID del gato.
>
> El formulario esta en el template index.html. Es un formulario HTML normal con method post y el token de seguridad csrf que Django exige. Cada pregunta tiene radio buttons con los IDs de las respuestas."

**Muestra:**
- En `urls.py`: las 3 rutas
- En `index.html`: la primera linea del form `<form method="post"...>` y `{% csrf_token %}`

---

### 5:45 - 6:45 → PANEL ADMIN + CRUD EN SQLITE

**Pantalla:** Navegador en `http://localhost:8000/admin`

**Acciones (en orden):**
1. Alt+Tab al navegador
2. Asegurate de que ya estes logueado en el admin
3. Haz clic en "Preguntas" en el menu izquierdo
4. Haz clic en cualquier pregunta (ej: la numero 1)
5. Edita el texto (agrega una palabra, por ejemplo cambia "explotó" por "explotó feo")
6. Baja y haz clic en "Save"
7. Vuelve a la app (`localhost:8000`) y recarga para mostrar que cambio

**Di esto mientras lo haces:**

> "El panel de administracion permite hacer CRUD completo sin escribir codigo. Aqui puedo ver todos los gatos, crear nuevos, editarlos o borrarlos. Lo mismo con las preguntas y respuestas.
>
> Voy a editar esta pregunta en vivo... le cambio el texto... guardo... y si vuelvo a la app, el cambio ya esta reflejado en la base de datos SQLite."

**Consejo:** Practica este paso una vez antes de grabar para que no te trabes.

---

### 6:45 - 7:45 → TESTS PASANDO

**Pantalla:** Terminal

**Acciones:**
1. Alt+Tab a la terminal donde tenias el comando listo
2. Corre exactamente este comando:

```bash
python manage.py test
```

3. Espera a que termine (toma unos 5 segundos)
4. Muestra el resultado: "Ran 3 tests... OK"

**Di esto:**

> "Para verificar que la logica funciona, escribi tests automaticos. Tengo tres pruebas: una que verifica que la pagina principal carga correctamente, otra que simula un usuario enviando el formulario, y otra que verifica que la pagina de resultado muestra el gato correcto.
>
> Los corro ahora..."

*(Espera a que termine)*

> "Listo, los tres tests pasaron. Esto me da confianza de que si hago cambios en el futuro, no voy a romper nada sin darme cuenta."

**Consejo:** Si por alguna razon falla un test, NO sigas grabando. Arreglalo primero.

---

### 7:45 - 9:00 → DESPLIEGUE Y REPOSITORIO

**Pantalla:** Navegador en tu repositorio de GitHub.

**Acciones:**
1. Alt+Tab al navegador
2. Ve a la pestana de GitHub (si ya la tienes abierta)
3. Muestra el repositorio
4. Si ya desplegaste en Render, abre la URL y muestrala

**Di esto:**

> "El codigo fuente esta en un repositorio publico de GitHub. Aqui pueden ver todos los archivos: los modelos, las vistas, los templates, los tests, todo.
>
> Ademas, la aplicacion esta desplegada en Render usando Gunicorn como servidor WSGI y SQLite como base de datos. Esta es la URL publica [muestra la URL o di la direccion]. Pueden probarla desde cualquier navegador."

**Si aun NO has subido a GitHub/Render:**

> "El proyecto esta listo para desplegar. Tengo el archivo requirements.txt con las dependencias y Gunicorn configurado. El siguiente paso es subirlo a GitHub y desplegarlo en Render."

---

### 9:00 - 10:00 → CONCLUSION

**Pantalla:** Vuelve a la app en `localhost:8000` o muestra tu cara.

**Di esto:**

> "En resumen, este proyecto integra todas las tematicas vistas en clase: creacion de modelos, manejo de UrlConf, vistas genericas, integracion de formularios, CRUD con SQLite a traves del panel admin, y testing automatico.
>
> Y lo mas importante: resuelve una problematica real que yo identifique como estudiante, que es la friccion grupal por estres no gestionado. El test no es un examen serio, es una herramienta de hielo roto para que los equipos se entiendan mejor.
>
> Gracias por ver el video."

---

## CHECKLIST FINAL (Imprimible)

Antes de apretar "Grabar", verifica:

- [ ] Servidor corriendo (`python manage.py runserver`)
- [ ] Datos cargados (`python manage.py seed`)
- [ ] Navegador en `localhost:8000` funciona
- [ ] Admin en `localhost:8000/admin` funciona (usuario: admin, pass: admin123)
- [ ] VS Code con zoom al 150%
- [ ] Archivos abiertos en VS Code: models.py, views.py, urls.py, tests.py
- [ ] Terminal lista con `python manage.py test` escrito pero sin correr
- [ ] WhatsApp cerrado
- [ ] Notificaciones del celular en silencio
- [ ] Grabacion en 1080p minimo

---

## SI ALGO FALLA DURANTE EL VIDEO

### El servidor se detuvo
Abre otra terminal y corre:
```bash
python manage.py runserver
```

### Los tests fallan
Di: "Dame un momento, voy a verificar..." y arreglalo fuera de camara. NO muestres tests fallidos.

### La pagina del admin no carga
Di: "El panel admin esta en /admin, aunque por tiempo no lo muestro ahora."

### No tienes la URL de Render todavia
Di: "El proyecto esta listo para desplegar. El repositorio esta en GitHub y el siguiente paso es subirlo a Render."

---

## TIEMPO TOTAL ESTIMADO: 9 min 30 seg

Margen de 30 segundos para imprevistos.
