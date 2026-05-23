# GUION PARA EL VIDEO (Maximo 10 minutos)

## Recomendacion: NO uses diapositivas formales

Lo mas efectivo es alternar entre:
1. **Navegador** (mostrar la app funcionando)
2. **VS Code** (mostrar el codigo mientras hablas)
3. **Terminal** (correr los tests)
4. **Panel Admin** (mostrar el CRUD)

Esto se ve mas profesional y dinamico. Solo asegurate de tener el zoom al 150% en el codigo para que se lea bien.

---

## 0:00 - 0:45 → INTRO + PROBLEMATICA (45 segundos)

**Pantalla:** Tu cara o la app abierta en el navegador.

**Di lo siguiente:**
> "Hola, mi nombre es [tu nombre] y este es mi proyecto final llamado 'Que Michi Eres'.
>
> La problematica que identifique es esta: en los grupos de trabajo universitario, especialmente en carreras tecnicas, cada persona maneja el estres de forma diferente. Hay quienes procrastinan, otros se paralizan, otros actuan como si nada pasara. El problema es que nunca paramos a identificar eso, y los grupos se desarman por friccion, no por falta de conocimiento.
>
> Mi app es un test de personalidad gamificado usando gatos memes, para que un grupo de estudiantes se entienda mejor y organice su ritmo de trabajo."

**Consejo:** No leas esto como robot. Dilo con tus palabras, como si se lo contaras a un amigo.

---

## 0:45 - 2:00 → DEMO DE LA APP FUNCIONANDO (1 min 15 seg)

**Pantalla:** Navegador con la app abierta en localhost.

**Di lo siguiente mientras haces clic:**
> "Voy a hacer el test. Aqui estan las 10 preguntas sobre situaciones universitarias reales. Voy a elegir algunas respuestas..."

*(Marca cualquier respuesta rapidamente y dale a "Descubrir mi Michi")*

> "Y el resultado me dice que soy... [el gato que salga]. Me muestra su imagen, su descripcion, y puedo hacer el test otra vez."

**Consejo:** No hagas el test completo, solo 2-3 preguntas rapido para no perder tiempo.

---

## 2:00 - 3:30 → MODELOS Y BASE DE DATOS (1 min 30 seg)

**Pantalla:** VS Code abierto en `testmichi/models.py`

**Di lo siguiente:**
> "Ahora les muestro como esta hecho por dentro. Empiezo con los modelos, que son las tablas de la base de datos. Tengo tres modelos:
>
> Gato, que guarda el nombre, la descripcion y la ruta de la imagen.
> Pregunta, que guarda el texto y el orden en que se muestra.
> Y Respuesta, que tiene dos llaves foraneas: una apunta a Pregunta y otra a Gato. Esto es una relacion muchos a uno. Muchas respuestas pertenecen a una pregunta, y muchas respuestas apuntan al mismo gato."

**Destaca con el cursor:**
- La clase `Gato`
- La clase `Respuesta` con sus dos `ForeignKey`
- El `class Meta` con `ordering` en Pregunta

**Consejo:** No expliques cada palabra, solo los conceptos clave.

---

## 3:30 - 5:00 → VISTAS GENERICAS (1 min 30 seg)

**Pantalla:** VS Code abierto en `testmichi/views.py`

**Di lo siguiente:**
> "Para las vistas use Vistas Genericas de Django. Tengo tres vistas:
>
> IndexView, que hereda de ListView. Esto significa que Django ya sabe como listar objetos. Yo solo le digo: usa el modelo Pregunta, este template, y ordénalas por el campo orden. Django hace la consulta a SQLite automaticamente.
>
> ResultadoView hereda de DetailView. Muestra un solo objeto, en este caso el gato ganador. Recibe el ID del gato por la URL y lo busca en la base de datos.
>
> Y ProcesarView hereda de View, que es la vista base. Aqui esta la logica personalizada: recibe las respuestas del formulario, cuenta cuantas veces salio cada gato usando Counter, y si hay empate elige uno al azar con random.choice."

**Destaca con el cursor:**
- `class IndexView(ListView)`
- `class ResultadoView(DetailView)`
- La parte de `Counter` y `random.choice` en ProcesarView

**Consejo:** Esto es lo mas importante del video. Asegurate de que se entienda que usaste vistas genericas.

---

## 5:00 - 5:45 → URLS Y FORMULARIOS (45 seg)

**Pantalla:** VS Code abierto en `testmichi/urls.py`

**Di lo siguiente:**
> "Las URLs estan en dos archivos. El principal incluye las rutas de nuestra app. Y dentro de testmichi tengo tres rutas: la raiz va a IndexView, procesar va a ProcesarView, y resultado recibe un numero que es el ID del gato.
>
> El formulario esta en el template index.html. Es un formulario HTML normal con method post y el token de seguridad de Django. Cada pregunta tiene radio buttons con los IDs de las respuestas."

**Muestra rapidamente:**
- `testmichi/urls.py`
- La primera linea del form en `index.html`

---

## 5:45 - 6:45 → PANEL ADMIN + CRUD (1 min)

**Pantalla:** Navegador en `/admin`

**Di lo siguiente mientras navegas:**
> "El panel de administracion de Django permite hacer CRUD completo sin escribir codigo. Aqui puedo ver todos los gatos, crear nuevos, editarlos o borrarlos. Lo mismo con las preguntas y respuestas. Les muestro como edito una pregunta en vivo..."

*(Entra a Preguntas, edita una, guarda)*

> "Listo, el cambio ya esta en la base de datos SQLite y se refleja inmediatamente en la app."

**Consejo:** Esta es la parte donde el profe se da cuenta de que usaste el admin bien.

---

## 6:45 - 7:45 → TESTS PASANDO (1 min)

**Pantalla:** Terminal abierta.

**Di lo siguiente:**
> "Para verificar que la logica funciona, escribi tests automaticos. Tengo tres pruebas: una que verifica que la pagina principal carga bien, otra que simula un usuario enviando el formulario, y otra que verifica que la pagina de resultado muestra el gato correcto."

*(Corre `python manage.py test` en la terminal)*

> "Ahi estan, los tres tests pasaron. Esto me da confianza de que si hago cambios en el futuro, no voy a romper nada sin darme cuenta."

**Consejo:** Asegurate de que la terminal se vea grande y clara.

---

## 7:45 - 9:00 → DESPLIEGUE Y REPOSITORIO (1 min 15 seg)

**Pantalla:** Navegador en GitHub (cuando lo subas) o mencionalo.

**Di lo siguiente:**
> "El codigo esta en un repositorio publico de GitHub y la aplicacion esta desplegada en Render. Aqui esta la URL publica [muestrala en pantalla o di la direccion]. La configure con Gunicorn como servidor WSGI y SQLite como base de datos."

*(Si ya tienes la URL de Render, muestra la app funcionando online)*

> "Pueden probarla desde el celular o cualquier navegador."

---

## 9:00 - 10:00 → CONCLUSION (1 min maximo)

**Pantalla:** Vuelve a la app o muestra tu cara.

**Di lo siguiente:**
> "En resumen, este proyecto cumple con todas las tematicas vistas en clase: modelos, vistas genericas, urls, formularios, CRUD con SQLite, panel admin y testing. Y lo mas importante: resuelve una problematica real que yo identifique como estudiante, que es la friccion grupal por estres no gestionado.
>
> Gracias por ver el video."

---

## CHECKLIST ANTES DE GRABAR

- [ ] Corre `python manage.py runserver` antes de empezar
- [ ] Corre `python manage.py seed` para tener los datos cargados
- [ ] Abre VS Code con zoom al 150%
- [ ] Abre la terminal lista para correr tests
- [ ] Abre el navegador en `/admin` con sesion iniciada
- [ ] Prueba la app una vez antes de grabar
- [ ] Cierra WhatsApp, notificaciones y pestanas innecesarias
- [ ] Graba en 1080p minimo

---

## TIEMPO TOTAL ESTIMADO: 9 min 30 seg

Te deja 30 segundos de margen para respirar o si te trabas en algo.
